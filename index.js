var express = require('express');
var bodyParser = require('body-parser');
var mqtt = require('./mqtt');
var cors = require("cors");
var app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

/*mqtt.client.on('connect', () => {
    setTimeout(() => {
        mqtt.writeLightingColorRGB(255,255,255);
        console.log("Wrote that bad boy");
    }, 1000);
});*/

app.listen(3000, () => {
    console.log("Server is listening");
});

app.use('/lighting', mqtt);