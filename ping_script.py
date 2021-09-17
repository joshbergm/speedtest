import sys
import subprocess
import datetime

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'speedtest-cli'])

from speedtest import Speedtest

# Settings
st = Speedtest()
st.get_best_server()
download_mbs = str(round(st.download() / 8000000, 2))  # 8000000 bits = 1 MB
download_mbits = str(round(st.download() / 1000000, 2))  # 1000000 bits = 1 Mbit
upload_mbs = str(round(st.upload() / 8000000, 2))  # 8000000 bits = 1 MB
upload_mbits = str(round(st.upload() / 1000000, 2))  # 1000000 bits = 1 Mbit

# print("<-------------------------->")
# print("Ping:" + "\nms: " + str(st.results.ping))
# print("")
# print("Download speed:" + "\nMB/s: " + download_mbs + "\nMbit/s: " + download_mbits)
# print("")
# print("Upload speed:" + "\nMB/s: " + upload_mbs + "\nMbit/s: " + upload_mbits)
# print("<-------------------------->")

current_time = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')  # Set current time for file name
with open('/path/to/folder/' + "UP_DOWNLOAD" + '_' + str(current_time) + '.txt',
          'w') as f:  # Open file to write data
    f.write("<-------------------------->")  # Fancy styling
    f.write("\n")  # New line
    f.write("Ping:" + "\nms: " + str(st.results.ping))
    f.write("\n\n")  # Insert blank rule
    f.write(("Download speed:" + "\nMB/s: " + download_mbs + "\nMbit/s: " + download_mbits))
    f.write("\n\n")  # Insert blank rule
    f.write(("Upload speed:" + "\nMB/s: " + upload_mbs + "\nMbit/s: " + upload_mbits))
    f.write("\n")  # New line
    f.write("<-------------------------->")  # Fancy styling
    f.close()  # close file
