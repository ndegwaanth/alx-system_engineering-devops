#!/usr/bin/node

const request = require('request');
// Import the 'request' module.

request.get(process.argv[2])
// Use the 'request' module to perform an HTTP GET request to the URL.

  .on('response', function (response) {
    // Set up an event listener for the 'response' event emitted by the HTTP request.

    console.log(`code: ${response.statusCode}`);
    // Log the HTTP status code of the response to the console.
  });
