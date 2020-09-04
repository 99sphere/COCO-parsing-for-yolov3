# COCO-parsing-for-yolov3
python3 code for parse COCO dataset to yolov3 format

## 1. cocotoyoloconverter.py
Download instances_train2017.json from the COCO website and put in the same directory as this script.   
In line 16, you should modify "car" to class that you want to extract like below.   
```(python3)
16 cat = "car"   
17 catIds = coco.getCatIds(catNms=[cat])
18 imgIds = coco.getImgIds(catIds=catIds )
19 images = coco.loadImgs(imgIds)
```

In line 32, you should modify "car_labels/" to directory name that you want to save result txt files.
```(python3)
32    with open("car_labels/" + filename, "a") as myfile:
33        for i in range(len(anns)):
34            xmin = anns[i]["bbox"][0]
35            ymin = anns[i]["bbox"][1]
36            xmax = anns[i]["bbox"][2] + anns[i]["bbox"][0]
37            ymax = anns[i]["bbox"][3] + anns[i]["bbox"][1]
```

After execute cocotoyoloconverter.py, A text file can be obtained for image files corresponding to class you enter at line 16.

## 2. compare.py

## 3. merge.py

## 4. listing.py

