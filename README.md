<img width="1567" height="333" alt="image" src="https://github.com/user-attachments/assets/93021798-b325-431d-b21d-cc9aeb6536ab" /># RunBoy-MP3-player
@ walkman inspired mp3 player that runs on linux using winamp themes built using a raspberry pi zero 2


<img width="2245" height="1587" alt="RUN-BOY" src="https://github.com/user-attachments/assets/b6dd8ea5-85c9-4ad7-b983-e53ee1914c1b" />

RunBoy is a Walkman-inspired MP3 player that runs on a Raspberry Pi Zero 2 using the Linux operating system. In addition, it can run old-school Winamp themes as it is designed to play music using the program QMMP. Any and all MP3s and music files played on this music player should be properly bought/licensed, which can be done from sites such as Bandcamp.

Why did I start this project? When I was trying to fix my old laptop by changing the operating system, I came across how certain music players compatible with Arch Linux could still run old vintage Winamp themes. These themes made me wonder if perhaps I could build an MP3 player that runs on Linux due to how lightweight it was as an operating system. I was also inspired by the look of old technology, particularly music players such as the Sony Walkman and early iPod competitors.

No custom PCB was needed for this project, as the parts are to be soldered to the GPIO pins or connected with bendable cables in order to make the device more compact and take up less space.

Dependencies and Drivers:
1. Raspberry Pi OS Lite (64-bit)
2. WM8960 Audio HAT driver
3. Capacitive Touch Display driver
4. Webamp skins
5. DFRobot example code and setup for UPS HAT
6. QMMP
7. gpiozero
8. gpio-pedal

links to guides for dependency and driver installation:

1. https://www.raspberrypi.com/software/operating-systems/
2. https://skins.webamp.org/
3. https://qmmp.ylsoftware.com/
4. https://wiki.dfrobot.com/dfr0528/docs/19884
5. https://www.elecrow.com/pub/wiki/2.8-inch_IPS_SPI_LCD_Capacitive_Touch_Display_Module_With_ILI9341_Driver-240x320_Resolution_Arduino_Compatible.html
6. https://www.waveshare.com/wiki/WM8960_Audio_HAT
7. https://gpiozero.readthedocs.io/en/stable/
8. https://pypi.org/project/gpio-pedal/
9. https://gist.github.com/shivasiddharth/6aba5fa187c8ce463259f18eb7171a1f#file-pi_encoder_volume-py
10. https://gist.github.com/SnoopTomm/6126b9ebb02bfc6efc2d0dcdfd4c44dd

Big thanks to @shivasiddharth for allowing me to use his pi_encoder_volume code ^___^


For the purposes of this build, I have designed a hybrid wiring schematic to showcase the design of the electronics.
<img width="1220" height="663" alt="Hybrid Wiring Schematic" src="https://github.com/user-attachments/assets/161fdfcc-3c10-455d-bc47-0dfa542f197d" />



To setup this device, Written setup instructions for the Operating System, Drivers, Music Player, and WINAMP themes, buttons, and volume knob can be found in the Setup Instructions Folder of this repository. The software folder contains a copy of a fork o f shivasiddharth's rotary encoder code adjusted for this build. the link to this code can be found here:
https://gist.github.com/SnoopTomm/6126b9ebb02bfc6efc2d0dcdfd4c44dd


INSERT A screenshot of a full 3D model of your case


(Disclaimer: I will have my friend 3d print the parts for me locally on his 3d printer so it is not included in the costs)
## Bill of Materials (BOM)

| Item | Quantity | Part | Description | Supplier | Link | Unit Price | Total |
|------|---------:|------|-------------|----------|------|-----------:|------:|
| 1 |1|Raspberry Pi Zero 2W kit|Micro-Computer|fastshippingmart|https://www.ebay.com/itm/188561108959?_skw=raspberry+pi+zero+2+w&itmmeta=01KX95805PABN6JVNN1KDTG1RZ&hash=item2be71e2fdf:g:aQcAAeSwxsNqPbLR&itmprp=enc%3AAQALAAAA8GfYFPkwiKCW4ZNSs2u11xBjF6NjBc1WOXsvrWXYbKlcGsfMWt1KHX19IL2rFkX%2F%2B2wY%2FgLB9PW0yvYMeAbc3vXlBDsMX%2FVxCRP8xwKp%2Fh2WZr59zB0Lzq0dqi9VwcO03RZzFQefesxN667vLRF43JESwvrcwuOkJp05I8QSUd3gzo8Lsy3%2F5xU2kkvqZU1DbH%2B12HTyDeaS7BWJm6ebFrtpGr75DMspnQ3Gre1prQEEL8%2FHfkPMvfL5hBEKIhgmWxwqlug3LW77CpPycRGgifBX1biJXq9zYn8wz4nlxVUL%2F%2BsJnvZlMq5v5WTypM4PHw%3D%3D%7Ctkp%3ABk9SR_6CoKXqZw|$13.90| |
| 2 |1|WM8960 Hi-Fi Sound Card HAT|Sound Card|Waveshare|https://www.waveshare.com/wm8960-audio-hat.htm|$18.99| |
| 3 |1|2.8inch IPS SPI LCD Touch Display Module|Display|Elecrow|https://www.elecrow.com/2-8-ips-spi-lcd-capacitive-touch-module-ili9341-driver-240-320-resolution.html|$10.90| |
| 4 |1|UPS HAT for Raspberry Pi Zero|Power Supply|DFRobot|https://www.dfrobot.com/product-1932.html|$19.90| |
| 5 |1|974058 3.7V 3000mAh LiPo Battery Lithium Polymer Batteries|Battery|YouTu Battery Store|https://www.aliexpress.us/item/3256809054033588.html|$14.99| |
| 6 |1|Soldering Iron Kit|Soldering Tools|KYZHXVO Store|https://www.amazon.com/Soldering-Adjustable-Temperature-Multimeter-Desoldering/dp/B09VXQ221K?sr=8-11|$16.99| |
| 7 |1|Degree Rotary Encoder EC11 Push Button|Volume knob|Connector Assemble Store|https://www.aliexpress.us/item/3256812453298792.html|$2.29| |
| 8 |1|Wire Silicone Insulation Tinned Copper|5 meter 28 AWG wire|Ammax Official Store|https://www.aliexpress.us/item/3256801334498498.html|$2.06| |
| 9 |1|Retro Foldable Over-ear Headphones Wired|Wired Headphones|Shenzhen Smile Technology|https://www.alibaba.com/product-detail/Retro-Foldable-Over-ear-Headphones-Wired_1601209006313.html|$24.28 (sample+shipping)| |
| 10 |1|Illuminated LED Toggle Switch|Power Switch|Connectore Store Store|https://www.aliexpress.us/item/3256808670191342.html|$4.07| |
| 11 |1|Long Header Jumper Wire|40pcs 10cm Female to Female Header Jumper Cables|Chanzon Store|https://www.amazon.com/Connector-Solderless-Multicolor-Electronic-Breadboard/dp/B09FPGT7JT?sr=8-7|$6.99| |
| 12 |2|Momentary Push Button|Buttons|FILN Online Store|https://www.aliexpress.us/item/1005009024025383.html|$3.53| |
| 13 |1|Patriot LX Series Micro SD Flash Memory Card 32GB|Storage|Patriot Memory Store|https://www.amazon.com/Patriot-Micro-Flash-Memory-Card/dp/B08KSSXKYR?sr=8-4|$13.49| |
| | |Estimated Shipping Costs + Tax|Shipping estimate to PO Box in Florida followed by carrier to Panama by sea (and tax estimate included)|MBE Panama|https://www.mbe-ca.com/|$40.00| |
| **Total** | | | | | | | **$192.38** |
