#!/usr/bin/env python3
import random, argparse

import re

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--scene", help="what scene to post in number")
args = parser.parse_args()

ls = []
scenes = {}
with open('montypython.txt', 'r') as f:
    scene_num = "1"
    for line in f:
        line = line.strip()
        temp_ls = []
        if (re.match(r"(Scene \b(([1-9])|(1[0-9])|(2[0-9])|(3[0-6]))\b)|(Narrative *)", line)):
            #print(scene_num)
            scene_num = line.replace(" ", "")
            scenes[scene_num] = []
        scenes[scene_num].append(line)


if (args.scene):
    scene_num = "Scene"+args.scene
    print("\n".join(scenes[scene_num]))

else:
    #print("getting here")
    print("\n".join(scenes[random.choice(list(scenes))])) 
    






