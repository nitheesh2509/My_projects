import wifi_qrcode_generator

qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid="FTTH-227350",hidden=False,authentication_type='WPA',password="ra4282227350"
)
qr_code.print_ascii()
qr_code.make_image().save('wifi.png')