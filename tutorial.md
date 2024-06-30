# Start to Finish Guide

## Collect Data
To collect data, use the `Imagemaker.py` file to record images. Press `q` to take the picture! This will automatically create a `resources` folder if it's not there, and many sub-folders as well.

## Label Data
You can use many different annotators, though I like using [labelImg](https://github.com/HumanSignal/labelImg). Just make sure that it is in the `.txt` or `yolo` format! Save these annotated files to the `/resources/labels/train` directory

## Train Data
Once you have your pictures and annotations, run the Train.py file and wait for it to finish. 

>Note: You may have to change your paths!

## Use The Model
Once you finish the step above, look in `runs/train<#>/weights` and you should see a `best.pt` file, copy that and paste it into the `src` directory. Run the `Detector.py` file using your new model!