#!/usr/bin/node
// print c according to number of argument given

const num = parseInt(process.argv[2]);

if (num) {
  let x = '';
  for (let i = 0; i < num; i++) {
    x += 'X';
  }

  let i = 0;
  while (i < num) {
    console.log(x);
    i++;
  }
} else {
  console.log('Missing size');
}
