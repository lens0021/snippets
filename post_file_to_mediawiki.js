#!/usr/local/bin/node
"use strict";

const WIKI_HOSTNAME = "127.0.0.1";
const TARGET_TITLE = "Gadget:TweetbotQuickEditor.js";
const EDIT_TOKEN = "+\\"; // As a anonymous user

const fs = require("fs");
const http = require("http");
const querystring = require("querystring");

const context = fs.readFileSync(`./${TARGET_TITLE}`).toString();

const data = querystring.stringify({
  action: "edit",
  title: TARGET_TITLE,
  text: context,
  token: EDIT_TOKEN
});
const req = http.request({
  hostname: WIKI_HOSTNAME,
  port: 80,
  path: "/api.php",
  method: "POST",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": Buffer.byteLength(data)
  }
});

req.write(data);
req.end();
