##This is a free software project named "SENSEable Shoes".
##Copyright (C) 2011 by Yen-Chia Hsu, CoDe LAB, Carnegie Mellon University, U.S.A.
##
##Permission is hereby granted, free of charge, to any person obtaining a copy of
##this software and associated documentation files (the "Software"), to deal in
##the Software without restriction, including without limitation the rights to
##use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
##of the Software, and to permit persons to whom the Software is furnished to do
##so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.

##########################
####      import      ####
##########################
import csv
import copy
import config as cf
##########################
####     functions    ####
##########################  
#### read all files    
def readFile():
    print "---------------------------------------------------------------------"
    print "construct data structure..."
    featureNumber = cf.config("featureNumber")
    labelName = cf.config("labelName")  
    dataset = {"data":[],"labelName":labelName}
    label = []
    for i in range(0,featureNumber):
        label.append([])
        
    ###############################################################
    #### usage:
    #### dataset["data"][label][feature]
    ###############################################################
    for i in range(0,len(labelName)):
        dataset["data"].append(copy.deepcopy(label))

    #### read files
    for idx_label in labelName:        
        #### read csv
        print "import dataset/train/"+labelName[idx_label]+".csv..."
        readTemp = None
        readTemp = csv.reader(open("dataset/train/"+labelName[idx_label]+".csv","rb"))
        for sample in readTemp:
            for i in range(0,len(sample)):
                dataset["data"][idx_label][i].append(float(sample[i]))

    #### return
    print "---------------------------------------------------------------------"
    return dataset
    
