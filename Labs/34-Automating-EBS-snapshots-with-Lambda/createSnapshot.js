"use strict";
console.log("Loading function");
var AWS = require("aws-sdk");
var ec2 = new AWS.EC2({ region: "us-west-2" });

exports.handler = (event, context, callback) => {
  var params = {
    VolumeId: event.volume,
  };
  ec2.createSnapshot(params, function (err, data) {
    if (err) {
      console.log(err, err.stack);
      callback(err, err.message);
    } else {
      console.log(data);
      callback(null, data);
    }
  });
};