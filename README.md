# COCO-parsing-for-yolov3
python3 code for parse COCO dataset to yolov3 format

## 1. cocotoyoloconverter.py
Download instances_train2017.json from the COCO website and put in the same directory as this script.   
At line 16, "car" to class that you want to extract like below.    
Class should be included in one of the 80 classes in coco names.

```(python3)
16 cat = "car"   
17 catIds = coco.getCatIds(catNms=[cat])
18 imgIds = coco.getImgIds(catIds=catIds )
19 images = coco.loadImgs(imgIds)
```

At line 32, modify "car_labels/" to directory name that you want to save result txt files.
```(python3)
32    with open("car_labels/" + filename, "a") as myfile:
33        for i in range(len(anns)):
34            xmin = anns[i]["bbox"][0]
35            ymin = anns[i]["bbox"][1]
36            xmax = anns[i]["bbox"][2] + anns[i]["bbox"][0]
37            ymax = anns[i]["bbox"][3] + anns[i]["bbox"][1]
```
After execute cocotoyoloconverter.py, text files will be saved in directory corresponding to class("car") you enter at line 16.

## 2. compare.py
Now, Save image files corresponding to txt files in directory that you entered at line 32 in cocotoyoloconverter.py.
At line 7, modify "person_lables" to directory name that you entered at line 32 in cocotoyoloconverter.py
```(python3)
6 path_0 = os.getcwd() + "/"
7 path_label = path_0 + "person_labels"
8 path_train = path_0 + "train2017"
```

At line 17, 18 and 28, modify "compare_result" to directory name that you want to save corresponding images. 
```(python3)
16 try:
17 	if not os.path.exists(path_0 + "compare_result"):
18 	       os.makedirs(path_0 + "compare_result")
19 except OSError:
20     print('Error: Creating directory of data')
```
After execute compare.py, Image files will be saved in directory("compare_reulst") corresponding to txt files.

## 3. mergy.py
Through the above two processes, an image, label file for a class can be obtained.
Now, put these together.


## 4. listing.py
Now, make listing file. This is needed for darknet train.
At line 04, modify "/03_eunbin" to your directory name.
```(python3)
04 path = os.getcwd() + "/03_eunbin"
```
When executed, the path corresponding to the jpg files in that folder is saved in the form of train.txt used for yolo training.
