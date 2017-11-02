#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:18:34 2017

@author: thvinmei
"""

import sys
import re

def Search_In_File(KeyWard,TargetFile):
    SettingFile = open(TargetFile)
    settings = SettingFile.readlines()
    SettingFile.close()
    answer_lines = ["NaN"] * len(settings)
     
    i = 0
    for line in settings:
        if line.find(KeyWard) >= 0:
            answer_lines[i] = line[:-1]
            i = i + 1

    return answer_lines

if __name__ == '__main__':
    character_name = str(sys.argv[1])
    target_file = str(sys.argv[2])
    target_charcter_bool = False
    target_parameter_setting_line = ''
    parameter_lines = Search_In_File("parameter",target_file)

    
    # search target character in parameter_lines
    for line in parameter_lines:
        if line.find(character_name+"=") >= 0:
            target_parameter_setting_line = str(line)
            break

    # if target character's type boolen...?
    if target_parameter_setting_line.find("logical") >= 0:
        target_charcter_bool = True
    

    if target_charcter_bool:
        # if target character is boolen type.
        # if it is note ".true", print "True".
        parameter_define_pattern= character_name+"="+r'\.true\.'
        answer = re.findall(parameter_define_pattern,target_parameter_setting_line)>[]
        print(answer)
    else:
        parameter_define_pattern= character_name+"="+r'([+-]?[0-9]+\.?[0-9]*)'
        answer = re.findall(parameter_define_pattern,target_parameter_setting_line)
        print(answer[0])
