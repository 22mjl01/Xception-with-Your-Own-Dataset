# Download the 56 zip files in Images_png in batches
import urllib.request
import tarfile
import os
import csv

CLASSES = ['Atelectasis', 'Cardiomegaly', 'Effusion', 'Infiltration', 'Mass', 'Nodule', 'Pneumonia', 'Pneumothorax',
           'Consolidation', 'Edema', 'Emphysema', 'Fibrosis', 'Pleural_Thickening', 'Hernia', 'No']
def prep():
  tar_path = "./tar_files"
  image_data_path = "./image_data"

  if not os.path.exists(tar_path):
    os.mkdir(tar_path)

  if not os.path.exists(image_data_path):
    os.mkdir(image_data_path)

  for _ in CLASSES:
    class_path = f'./image_data/{_}'
    if not os.path.exists(class_path):
      os.mkdir(class_path)


def download_chestxray14():
  # URLs for the zip files
  links = [
      'https://nihcc.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz',
    #   'https://nihcc.box.com/shared/static/i28rlmbvmfjbl8p2n3ril0pptcmcu9d1.gz',
    #   'https://nihcc.box.com/shared/static/f1t00wrtdk94satdfb9olcolqx20z2jp.gz',
    # 'https://nihcc.box.com/shared/static/0aowwzs5lhjrceb3qp67ahp0rd1l1etg.gz',
    #   'https://nihcc.box.com/shared/static/v5e3goj22zr6h8tzualxfsqlqaygfbsn.gz',
    # 'https://nihcc.box.com/shared/static/asi7ikud9jwnkrnkj99jnpfkjdes7l6l.gz',
    # 'https://nihcc.box.com/shared/static/jn1b4mw4n6lnh74ovmcjb8y48h8xj07n.gz',
    #   'https://nihcc.box.com/shared/static/tvpxmn7qyrgl0w8wfh9kqfjskv6nmm1j.gz',
    # 'https://nihcc.box.com/shared/static/upyy3ml7qdumlgk2rfcvlb9k6gvqq2pj.gz',
    # 'https://nihcc.box.com/shared/static/l6nilvfa9cg3s28tqv1qc1olm3gnz54p.gz',
    # 'https://nihcc.box.com/shared/static/hhq8fkdgvcari67vfhs7ppg2w6ni4jze.gz',
    # 'https://nihcc.box.com/shared/static/ioqwiy20ihqwyr8pf4c24eazhh281pbu.gz'
  ]
  fns = []



  for idx, link in enumerate(links):
      fn = './tar_files/images_%02d.tar.gz' % (idx+1)
      print('downloading'+fn+'...')
      urllib.request.urlretrieve(link, fn)  # download the zip file
      fns.append(fn)

  return fns


  print("Download complete. Please check the checksums")


def move_files():
  # image folder dir
  folder_dir = './image_data/images'


  i = 0
  with open('./Data_Entry_2017_v2020.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
        if row[0] == 'Image':
          continue
        if i > 5000:
          break
        parsed_row = row[0].split(',')
        img_name, labels = parsed_row[0], parsed_row[1].split('|')

        for _ in labels:
          try:
            os.rename(f'{folder_dir}/{img_name}', f'./image_data/{_}/{img_name}')
          except(Exception):
            continue
        i+= 1



prep()
fns = download_chestxray14() # you may have to comment this out and manually replace it with [images_01.tar.gz]

# extract files
for fn in fns:
  open_tar = tarfile.open(fn, 'r')
  open_tar.extractall('./image_data')


move_files()