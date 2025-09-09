import pydicom as dicom
import matplotlib.pylab as plt
import os

########################################
## GDrive
# !pip install pydicom
# !pip install matplotlib

# from google.colab import drive
# drive.mount('/content/gdrive')
# myPath = 'gdrive/My Drive/CPAISD Core-Penumbra Acute Ischemic Stroke Dataset/train/2.25.112612366789117279937831792836336427905'

## Local
local_path = ''
myPath = f'{local_path}/CPAISD Core-Penumbra Acute Ischemic Stroke Dataset/train/2.25.112612366789117279937831792836336427905'

########################################
## Get all subfolders
all_folders = os.listdir(myPath)
all_folders.sort()

## For all subfolders
for f in all_folders:
    image_path = f'{myPath}/{f}/raw.dcm'

    ##########
    try:
        ds = dicom.dcmread(image_path)
    except:
        continue

    arr = ds.pixel_array

    plt.imshow(arr, cmap="gray")
    plt.savefig(f'{myPath}/{f}.png')

    