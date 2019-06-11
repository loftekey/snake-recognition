import requests, os, imghdr
import logging, time
from lxml import etree
from threading import Thread


start_time = time.time()
input_path = "./snake"
dirname = "./ndata"

def download_image(url, path):
	try:
		response = requests.get(url, timeout=10)
		if response.status_code == 200:
			if (response.headers['content-type'] == "image/jpeg"):
				img = response.content
				with open(path, 'wb') as f:
					f.write(img)
					logging.info(path)
			# file_type = imghdr.what(path)
	except Exception as ex:
		print(ex, url)

i = 0
flag = True
i_list = []
for fname in os.listdir(input_path):
	if fname.endswith(".txt"):
		fpath = os.path.join(input_path, fname)
		label = fname.split(".")[0]
		threads = []
		tem_i = 0
		for line in open(fpath, "r", encoding="utf-8"):
			i = i + 1
			tem_i = tem_i + 1
			i_list = line.split(" ")
			img_url = i_list[1]
			img_name = "_".join([label, i_list[0].split("_")[1]])
			img_name = "".join([img_name, ".jpg"])
			img_save_path = os.path.join(dirname, img_name)
			t = Thread(target = download_image, args = [img_url, img_save_path])
			t.start()
			threads.append(t)
		for t in threads:
			t.join()

end_time = time.time()
print("Execution time: ", "%.2f" % (end_time - start_time) + " s")