#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

function computeCompletedTasks (apiUrl) {
  request(apiUrl, function (error, response, body) {
    if (error) {
      console.error('Error:', error);
    } else if (response && response.statusCode !== 200) {
      console.error('Invalid status code:', response.statusCode);
    } else {
      const tasks = JSON.parse(body);
      const completedTasksByUser = {};

      tasks.forEach(task => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });
      console.log(completedTasksByUser);
    }
  });
}

if (apiUrl) {
  computeCompletedTasks(apiUrl);
} else {
  console.error('Usage: node 6-completed_tasks.js <API-URL>');
}
