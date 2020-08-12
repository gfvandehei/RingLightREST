var express = require('express');
var router = express.Router();

router.use("/ringlight", require("./ringlight"));

module.exports = router
//exports.client = client
//exports.writeLightingColorRGB = writeLightingColorRGB