var mqtt = require('mqtt');
var client  = mqtt.connect('mqtt://localhost');

var express = require('express');
var router = express.Router();

client.on("connect", () => {
    console.log("Connected to MQTT broker");
});

function writeLightingColorRGB(r, g, b){
    object = {
        "effected_lights": ["ring_light"],
        "message_type": "set_single_color",
        "color_format": "rgb",
        "color": [r, g, b]
    }

    client.publish('home/lighting', JSON.stringify(object));
    console.log("Here");
}

router.post("/singlecolor", (req, res) => {
    let body = req.body;
    console.log(req.body);
    body = body['rgb'];
    console.log(req.body);
    let r = parseInt(body[0]);
    let g = parseInt(body[1]);
    let b = parseInt(body[2]);
    
    writeLightingColorRGB(r, g, b);
    res.send(["OK!"]);
});

module.exports = router
//exports.client = client
//exports.writeLightingColorRGB = writeLightingColorRGB