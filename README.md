# RunBoy-MP3-player
@ walkman inspired mp3 player that runs on linux using winmap themes built using a raspberry pie zero 2

RunBoy is a walkman inspired mp3 player that runs on a raspberry pi zero 2 using the Linux opperating system. In adition, it can run oldschool winamp themes as its decined to play music using the program QMMP. Any and all mp3s and music files played on this music player should be properly bought/liscenced, which can be done from sites such as bandcamp.

Why did I start this project? When I was trying to fix my old laptop by changing the opperating system, I came across how certain music playerscompatible with arcg linux could still run old vintage winamp themes. These themes made me wonder i perhaps I could build an MP3 player that runs on Linux, due to how lightweoght it was as an Operating system. I was also inspired by the look of old technology, particularly music players such ass the sony walkman and early ipod competitors.

No PCB was designed for this project, as pieces are to be soldered to the pins or connected with bendable cables in order to make the device more compact.

Software development for the buttons and the setup of drivers is in progress, although on hold until components arive and can be tested.

Dependencies and Drivers:
1. Raspberry Pi OS Lite (64-bit)
2. WM8960 Audio HAT driver
3. Capacitive Touch Display driver
4. webamp skins
5. DFRobot example code and setup for UPS HAT
6. QMMP
7. gpiozero

links to guides for dependency and driver instalation:

1. https://www.raspberrypi.com/software/operating-systems/
2. https://skins.webamp.org/
3. https://qmmp.ylsoftware.com/
4. https://wiki.dfrobot.com/dfr0528/docs/19884
5. https://www.elecrow.com/pub/wiki/2.8-inch_IPS_SPI_LCD_Capacitive_Touch_Display_Module_With_ILI9341_Driver-240x320_Resolution_Arduino_Compatible.html
6. https://www.waveshare.com/wiki/WM8960_Audio_HAT
7. https://gpiozero.readthedocs.io/en/stable/









For the purposes of this build i have designed a hybrid wiring schematic to showcase the design of the electronic


A screenshot of a full 3D model with your project



## Bill of Materials (BOM)

| Item | Quantity | Part | Description | Supplier | Link | Unit Price | Total |
|------|---------:|------|-------------|----------|------|-----------:|------:|
| 1 |1|Raspberry Pi Zero 2W with Header|Micro-Computer|Adafruit|https://www.adafruit.com/product/6008|$19.80| |
| 2 |1|WM8960 Hi-Fi Sound Card HAT|Sound Card|Waveshare|https://www.waveshare.com/wm8960-audio-hat.htm|$18.99| |
| 3 |1|2.8inch IPS SPI LCD Touch Display Module|Display|Elecrow|https://www.elecrow.com/2-8-ips-spi-lcd-capacitive-touch-module-ili9341-driver-240-320-resolution.html|$10.90| |
| 4 |1|UPS HAT for Raspberry Pi Zero|Power Supply|DFRobot|https://www.dfrobot.com/product-1932.html|$19.90| |
| 5 |1|974058 3.7V 3000mAh Lipo Battery Lithium Polymer Batteries|Battery|YouTu Battery Store|https://www.aliexpress.us/item/3256809054033588.html|$14.99| |
| 6 |1|Soldering Iron Kit|Soldering Tools|KYZHXVO Store|https://www.amazon.com/Soldering-Adjustable-Temperature-Multimeter-Desoldering/dp/B09VXQ221K?sr=8-11|$16.99| |
| 7 |1|Degree Rotary Encoder EC11 Push Button|volume knob|Connector Assemble Store|https://www.aliexpress.us/item/3256812453298792.html|$2.29| |
| 8 |1|Wire Silicone Insulation Tinned Copper|5 meter 28 AWG wire|Ammax Official Store|https://www.aliexpress.us/item/3256801334498498.html|$2.06| |
| 9 |1|Retro Foldable Over-ear Headphones Wired|Wired Headphones|Shenzhen Smile Technology|https://www.alibaba.com/product-detail/Retro-Foldable-Over-ear-Headphones-Wired_1601209006313.html|$24.28 (sample+shipping)| |
| 10 |1|Illuminated Led Toggle Switch|Power Switch|Connectore Store Store|https://www.aliexpress.us/item/3256808670191342.html|$4.07| |
| 11 |1|Long Header Jumper Wire|40pcs 10cm Female to Female Header Jumper Cables|Chanzon Store|https://www.amazon.com/Connector-Solderless-Multicolor-Electronic-Breadboard/dp/B09FPGT7JT?sr=8-7|$6.99| |
| 12 |2|Momentary Push Button|Buttons|FILN Online Store|https://www.aliexpress.us/item/1005009024025383.html|$3.53| |
| 13 |1|Patriot LX Series Micro SD Flash Memory Card 32GB|Storage|patriot Memory Store|https://www.amazon.com/Patriot-Micro-Flash-Memory-Card/dp/B08KSSXKYR?sr=8-4|$13.49
| |
|  ||Estimated Shipping Costs + Tax|Shipping estimate to PO Box in Florida followed by carrier to Panama by sea (and tax estimate included)|MBE Panama|https://www.mbe-ca.com/|$40.00| |
| **Total** | | | | | | | **$198.28** |
