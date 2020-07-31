import pandas as pd
import requests
dataframe = pd.read_csv('s.csv')
dir = 'downloaded_images/'
img_links = dataframe.iloc[:,:]
img_numbers = list(range(0, 129000))

for i,url in enumerate(img_links['image_url']):
    print('Downloading Image\t{0}'.format(img_numbers[i]))
    image=requests.get(url, stream=True)
    if image.status_code==200:
        with open(dir+'image_'+str(img_numbers[i])+'.jpg','wb')as f:
            for chunk in image.iter_content(1024):
                f.write(chunk)


