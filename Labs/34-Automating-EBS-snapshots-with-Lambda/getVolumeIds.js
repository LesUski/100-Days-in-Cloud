"use strict";
console.log("Loading function");
var AWS = require("aws-sdk");
var ec2 = new AWS.EC2({ region: "us-west-2" });
var lambda = new AWS.Lambda();

exports.handler = (event, context, callback) => {
  ec2.describeVolumes(null, function (err, data) {
    if (err) {
      console.log(err, err.stack);
      callback(err, err.stack);
    } else {
      for (var i = 0; i < data.Volumes.length; i++) {
        var params = {
          FunctionName: "TakeEbsSnapshot", //Or the name of the function you created
          Payload: JSON.stringify({ volume: data.Volumes[i].VolumeId }),
          LogType: "Tail",
        };

        lambda.invoke(params, function (err, data) {
          if (err) {
            console.log(err, err.stack);
            callback(err, err.stack);
          } else {
            console.log(data);
          }
        });
      }
    }
  });
};
