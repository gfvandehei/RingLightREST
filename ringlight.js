var express = require('express');
var router = express.Router();
var client = require("./mqtt");

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

function writeLightingFrame(frameData){
    object = {
        "effected_lights": ["ring_lights"],
        "message_type": "set_frame",
        "frame": frameData
    }

    client.publish("home/lighting", JSON.stringify(object));
    console.log("Published lighting frame");
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

router.post("/multicolor", (req, res) => {
    let body = req.body;
    console.log(`Recieved multicolor request with body ${req.body}`);
    let frame = body['frame'];

    if(frame.length != 36){ //36 is the number of LED's in a ring light
        return res.sendStatus(400).send("Incorrect frame length");
    }
    res.send(["OK!"]);
});

module.exports = router
//exports.client = client
//exports.writeLightingColorRGB = writeLightingColorRGB