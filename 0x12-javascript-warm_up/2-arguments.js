#!/usr/bin/node

import { argv } from 'node:process';

if (argv.length === 0) {
  console.log('No argument');
} else if (argv.length === 1) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
