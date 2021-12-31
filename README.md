# kRP: kRememberPasswords

## Introduction

This GitHub repo was created to backup my password creation and management tools, which I have developed in order to secure my own passwords and practice writing programs involving cryptogpaphic algorithms.

## Randomizer

kRandomPassword (krp.py) was the first program I wrote for this repository.  It generates a random password using the ```secrets``` python module.

## Translator

Translator (```tra2.py```) uses a randomly generated key from ```mkk.py``` and uses that key to convert any basic password into a long and hard-to-guess string.  The script was developed to make long and secure passwords easy-to-remember by generating them from a catchphrase.  The key functions as a master password: you will need it to know any password generated with it.


