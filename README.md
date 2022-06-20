## insect detection api

-this is an api used for detect and count the number of to types of insects namely the Mediterranean fruit fly and the peach fruit fly,(Ceratitis Capitata, Bactrocera Zonata)

-The detection is done by volov5 with accuracy 84%.

-you can use our version by sending a post request with the photo you want to know the count of each type of insects to this link (http://insect-detection-api.azurewebsites.net/detect).

    -Example of returned data

    {
    "cod": 200,
    "message": "Image Uploaded Successfully",
    "n_bz": "2",
    "n_cc": "3",
    "results": [
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
        }
    ]

    }

# you also can clone this rebo and do the following to get your local system ready:

-after cloning the rebo go to the folder and install all the requirements by running this code on your cmd `pip install -r requirements.txt`  
-now download the model from this [link](https://drive.google.com/file/d/1mtpDq-_TFdypufCNwQtvprMfqbZeBs46/view?usp=sharing) to the main folder.  
-run app.py and use your localhost link with detect route for post requests.
