import re
####################################################
fileIn = "tcl/base_bd.tcl" 
fileOut = "../redpitaya-125-14/1.0/preset.xml"
lineStart = 210 #first line to parse
lineStop = 616  #last line to parse
####################################################

#Prepare file pointers
fOut=open(fileOut,"w+")
fIn=open(fileIn,"r")
for i in range(lineStart - 1):
    fIn.readline()

#Preset Header
fOut.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
fOut.write('<ip_presets schema="1.0">\n')
fOut.write('<ip_preset preset_proc_name="ps7_preset">\n')
fOut.write('<ip vendor="xilinx.com" library="ip" name="processing_system7" version="*">\n')
fOut.write('<user_parameters>\n')

#Preset Config PS
for i in range(lineStop - lineStart + 1):
    line = fIn.readline()
    name = re.findall("CONFIG\.\w+", line)[0]
    value = re.findall("{(.+?)}", line)[0]
    if value != "<Select>":
        fOut.write('<user_parameter name="{}" value="{}"/>\n'.format(name, value))

#Preset Footer
fOut.write('</user_parameters>\n')
fOut.write('</ip>\n')
fOut.write('</ip_preset>\n')
fOut.write('</ip_presets>\n')

#Close file pointers
fOut.close()
fIn.close()