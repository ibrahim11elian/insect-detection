## insect detection api

-this is an api used for detect and count the number of to types of insects namely the Mediterranean fruit fly and the peach fruit fly,(Ceratitis Capitata, Bactrocera Zonata)

-The detection is done by volov5 with accuracy 95%/.

-you can use our version by sending a post request with the photo you want to know the count of each type of insects to this link (http://insect-detectoin-api.azurewebsites.net/detect).

    -Example of returned data

    {
    "cod": 200,
    "message": "Image Uploaded Successfully",
    "n_bz": "12",
    "n_cc": "13",
    "results": [
        {
            "COORDINATES": {
                "xmax": 569,
                "xmin": 488,
                "ymax": 644,
                "ymin": 551
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9635071754
        },
        {
            "COORDINATES": {
                "xmax": 224,
                "xmin": 129,
                "ymax": 564,
                "ymin": 469
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.961155355
        },
        {
            "COORDINATES": {
                "xmax": 92,
                "xmin": 6,
                "ymax": 430,
                "ymin": 350
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9565539956
        },
        {
            "COORDINATES": {
                "xmax": 148,
                "xmin": 61,
                "ymax": 547,
                "ymin": 453
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9561279416
        },
        {
            "COORDINATES": {
                "xmax": 843,
                "xmin": 743,
                "ymax": 141,
                "ymin": 46
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.954942286
        },
        {
            "COORDINATES": {
                "xmax": 648,
                "xmin": 578,
                "ymax": 798,
                "ymin": 711
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9541110992
        },
        {
            "COORDINATES": {
                "xmax": 160,
                "xmin": 72,
                "ymax": 361,
                "ymin": 264
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9532185793
        },
        {
            "COORDINATES": {
                "xmax": 496,
                "xmin": 415,
                "ymax": 662,
                "ymin": 602
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9519825578
        },
        {
            "COORDINATES": {
                "xmax": 175,
                "xmin": 87,
                "ymax": 750,
                "ymin": 653
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9507207274
        },
        {
            "COORDINATES": {
                "xmax": 212,
                "xmin": 123,
                "ymax": 1174,
                "ymin": 1078
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9481058717
        },
        {
            "COORDINATES": {
                "xmax": 427,
                "xmin": 349,
                "ymax": 637,
                "ymin": 588
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9479878545
        },
        {
            "COORDINATES": {
                "xmax": 668,
                "xmin": 586,
                "ymax": 1012,
                "ymin": 935
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9473797083
        },
        {
            "COORDINATES": {
                "xmax": 212,
                "xmin": 126,
                "ymax": 967,
                "ymin": 885
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9456249475
        },
        {
            "COORDINATES": {
                "xmax": 765,
                "xmin": 687,
                "ymax": 405,
                "ymin": 352
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.943428874
        },
        {
            "COORDINATES": {
                "xmax": 324,
                "xmin": 241,
                "ymax": 629,
                "ymin": 570
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9402990937
        },
        {
            "COORDINATES": {
                "xmax": 824,
                "xmin": 764,
                "ymax": 768,
                "ymin": 667
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9375731945
        },
        {
            "COORDINATES": {
                "xmax": 745,
                "xmin": 703,
                "ymax": 795,
                "ymin": 747
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9324370027
        },
        {
            "COORDINATES": {
                "xmax": 427,
                "xmin": 363,
                "ymax": 990,
                "ymin": 892
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9317911863
        },
        {
            "COORDINATES": {
                "xmax": 538,
                "xmin": 475,
                "ymax": 254,
                "ymin": 198
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.9313057661
        },
        {
            "COORDINATES": {
                "xmax": 688,
                "xmin": 626,
                "ymax": 626,
                "ymin": 526
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.927638948
        },
        {
            "COORDINATES": {
                "xmax": 341,
                "xmin": 263,
                "ymax": 510,
                "ymin": 452
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.919265449
        },
        {
            "COORDINATES": {
                "xmax": 273,
                "xmin": 204,
                "ymax": 722,
                "ymin": 637
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.9018700719
        },
        {
            "COORDINATES": {
                "xmax": 575,
                "xmin": 475,
                "ymax": 217,
                "ymin": 149
            },
            "DETECTION_TYPE": "BZ",
            "SCORE": 0.8715131283
        },
        {
            "COORDINATES": {
                "xmax": 58,
                "xmin": 0,
                "ymax": 878,
                "ymin": 804
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.8675023317
        },
        {
            "COORDINATES": {
                "xmax": 272,
                "xmin": 204,
                "ymax": 724,
                "ymin": 635
            },
            "DETECTION_TYPE": "CC",
            "SCORE": 0.8475272059
        }
    ]

    }

-you also can clone this rebo and do the following to git your local system ready:  
 -after cloning the rebo go to the folder and install all the requirements by running this code on your cmd `pip install -r requirements.txt`
-now download the model from this [link](https://drive.google.com/file/d/1Nzx8kAejq2rz6yv2YAyOXlp4iFcX8Mf6/view?usp=sharing) to the main foldder.
-run app.py and use your localhost link with detect route for post requests.
