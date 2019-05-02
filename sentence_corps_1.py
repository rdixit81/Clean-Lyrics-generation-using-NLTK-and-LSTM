#!/usr/bin/env python
# -*- coding: utf-8 -*- 
training_data = []
lines = [line.rstrip('\n') for line in open('test.txt')]
for i in range(len(lines)):
    training_data.append({"class":"negative","sentence": lines[i]})
lines = [line.rstrip('\n') for line in open('positive.txt')]

#print ("%s sentences of training data" % len(training_data))
