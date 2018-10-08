#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('/usr/lib/node_modules/blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const button = 'P9_25';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(button, b.INPUT);

const LED1 = 'P9_14';
b.pinMode(LED1, b.OUTPUT);
//b.analogWrite(LED1, duty_cycle);

const AUTH = 'f757737db5574b37903bfd22e8d98498';


var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);
var v4 = new blynk.VirtualPin(4);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v4.on('write', function(param) {
    console.log('V4:', param[0]);
    b.analogWrite(LED1, param[0]/1023);
});
v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();
}
