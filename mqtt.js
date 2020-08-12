var mqtt = require('mqtt');
var client  = mqtt.connect('mqtt://localhost');

client.on("connect", () => {
    console.log("Connected to MQTT broker");
});

module.exports = client;
//exports.client = client
//exports.writeLightingColorRGB = writeLightingColorRGB