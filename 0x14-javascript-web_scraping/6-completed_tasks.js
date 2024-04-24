#!/usr/bin/node
/*
 * This a script that computes the number of tasks completed by user id.
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 * You must use the module request
 */

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasksByUserId = {};

  tasks.forEach((task) => {
    const userId = task.userId;
    const taskId = task.id;
    const completed = task.completed;

    if (completed) {
      if (!completedTasksByUserId[userId]) {
        completedTasksByUserId[userId] = 1;
      } else {
        completedTasksByUserId[userId]++;
      }
    }
  });

  console.log(completedTasksByUserId);
});
