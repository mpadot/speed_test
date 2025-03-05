import speedtest

st = speedtest.Speedtest()
download_speed = st.download()


upload_speed = st.upload()

ping = st.results.ping

print("Your download speed is: ", download_speed)
print("Your upload speed is: ", upload_speed)
print("Your ping is: ", ping)


