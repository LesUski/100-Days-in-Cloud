const cdk = require("@aws-cdk/core");
const s3 = require("@aws-cdk/aws-s3");
const iam = require("@aws-cdk/aws-iam");
const lambda = require("@aws-cdk/aws-lambda");
const lambdaEventSource = require("@aws-cdk/aws-lambda-event-sources");
const dynamodb = require("@aws-cdk/aws-dynamodb");

const imageBucket = "cdk-rekn-imagebucket";

class CdkAppStack extends cdk.Stack {
    /**
     *
     * @param {cdk.Construct} scope
     * @param {string} id
     * @param {cdk.StackProps=} props
     */
    constructor(scope, id, props) {
        super(scope, id, props);

        // The code that defines your stack goes here

        // ========================================
        // Bucket for storing images
        // ========================================
        const bucket = new s3.Bucket(this, imageBucket, {
            removalPolicy: cdk.RemovalPolicy.DESTROY,
        });
        new cdk.CfnOutput(this, "Bucket", { value: bucket.bucketName });

        // ========================================
        // Role for AWS Lambda
        // ========================================
        const role = new iam.Role(this, "cdk-rekn-lambdarole", {
            assumedBy: new iam.ServicePrincipal("lambda.amazonaws.com"),
        });
        role.addToPolicy(
            new iam.PolicyStatement({
                effect: iam.Effect.ALLOW,
                actions: [
                    "rekognition:*",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                ],
                resources: ["*"],
            })
        );

        // ========================================
        // DynamoDB table for storing image labels
        // ========================================
        const table = new dynamodb.Table(this, "cdk-rekn-imagetable", {
            partitionKey: { name: "Image", type: dynamodb.AttributeType.STRING },
            removalPolicy: cdk.RemovalPolicy.DESTROY,
        });
        new cdk.CfnOutput(this, "Table", { value: table.tableName });

        // ========================================
        // AWS Lambda function
        // ========================================
        const lambdaFn = new lambda.Function(this, "cdk-rekn-function", {
            code: lambda.AssetCode.fromAsset("lambda"),
            runtime: lambda.Runtime.PYTHON_3_8,
            handler: "index.handler",
            role: role,
            environment: {
                TABLE: table.tableName,
                BUCKET: bucket.bucketName,
            },
        });
        lambdaFn.addEventSource(
            new lambdaEventSource.S3EventSource(bucket, {
                events: [s3.EventType.OBJECT_CREATED],
            })
        );

        bucket.grantReadWrite(lambdaFn);
        table.grantFullAccess(lambdaFn);
    }
}

module.exports = { CdkAppStack };