---
title: RunBoy
author: Tomas Mesa
description: Runboy is a portable mp3 player that runs on the linux operating system
created at: 02-10-2026
---

# July 10: brainstormed and created prototype design
I spent the day mostly sketching and brainstorming what my device would look like as well as researching the parts i would likely need in order to build it. I decided in using QMMP as the main interface of my device as it can run oldschool winamp skins. I also decided to try both Raspberry Pi OS and arch linux ARM depending on their stability on the device.

<img width="2492" height="1592" alt="image" src="https://github.com/user-attachments/assets/2c5355e7-a181-4384-baef-72d82e417924" />
<img width="2495" height="1589" alt="image" src="https://github.com/user-attachments/assets/925470ad-f949-4f54-97d9-ed2545f8a9e2" />

the follwing list details the parts i need and where i plan to buy them from:
1. https://www.addicore.com/products/mt3608-step-up-adjustable-dc-dc-switching-boost-converter
2. https://www.addicore.com/products/tp4056-tc4056a-lithium-battery-charger-and-protection-module
3. https://www.adafruit.com/product/2011
4. https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/
5. https://thepihut.com/products/full-length-heatsink-for-raspberry-pi-zero
6. https://www.waveshare.com/product/raspberry-pi/3.5inch-rpi-lcd-c.htm
7. https://thepihut.com/products/hifiberry-dac-zero
8. https://www.amazon.com/Koss-KPH30iw-Headphones-Microphone-Lightweight/dp/B075FDCYFD
9. https://www.amazon.com/DaierTek-Toggle-Switch-Automotive-Industrial/dp/B0GCHGP5S9?sr=8-1
10. https://www.amazon.com/22-AWG-Electronic-Wire-6PK/dp/B0DNQC9HMV
11. https://www.adafruit.com/product/3814
12. https://www.adafruit.com/product/261
13. https://www.adafruit.com/product/5263
14. https://www.amazon.com/AstroAI-Digital-Multimeter-Voltage-Tester/dp/B01ISAMUA6?sr=8-6
15. https://www.amazon.com/ANBES-Soldering-Iron-Kit-Electronics/dp/B06XZ31W3M
16. https://www.sparkfun.com/gpio-header-male-pth-0-1in-2x20-pin.html
17. https://www.amazon.com/Bawofu-Supply-Charger-Adapter-Universal/dp/B0BSF3TB8P?sr=8-3
18. https://www.amazon.com/Patriot-Micro-Flash-Memory-Card/dp/B08KSSXKYR?sr=8-16

<img width="1523" height="789" alt="image" src="https://github.com/user-attachments/assets/b3282cab-b3fb-462b-a7c6-487ad1c956b7" />


controls i might add afterwards (less necessary):
1. skip button
2. play button
3. previous button

# July 11: Streamlined design, created neater sketches of parts and casing, changed parts used for the product to work.

I spent the day researching more effective parts to use for this project that would minimize the size of the mp3 player, further research aslo allowed me to removie conflicting parts, unnecesary cables, find cheaper alternatives to parts, and create an overall better build. In addition i designed a prototype shell that may be subject to further change

Heres the improved list of parts (RunBoy 2.0):
1. https://www.adafruit.com/product/6008
2. https://www.waveshare.com/wm8960-audio-hat.htm
3. https://www.elecrow.com/2-8-ips-spi-lcd-capacitive-touch-module-ili9341-driver-240-320-resolution.html
4. https://www.dfrobot.com/product-1932.html
5. https://www.aliexpress.us/item/3256809054033588.html?spm=a2g0o.productlist.main.9.313eCYZmCYZmZm&aem_p4p_detail=202607102232262157500981886800007304693&algo_pvid=b1e3cc77-1e6c-4e41-82ce-3de99637d10c&algo_exp_id=b1e3cc77-1e6c-4e41-82ce-3de99637d10c-8&pdp_ext_f=%7B%22order%22%3A%221013%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%2114.99%216.99%21%21%2114.99%216.99%21%40212a6e2917837479466934107e61a3%2112000048437368273%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Acbbf39d4%3Bm03_new_user%3A-29895%3BpisId%3A5000000207262906&curPageLogUid=7OM6lVLHFe1L&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009240348340%7C_p_origin_prod%3A&search_p4p_id=202607102232262157500981886800007304693_7
6. https://www.aliexpress.us/item/3256808670191342.html?spm=a2g0o.productlist.main.15.15e36ac1qX1hFa&algo_pvid=1998479f-e8a5-45b0-8fe7-877f3058d815&algo_exp_id=1998479f-e8a5-45b0-8fe7-877f3058d815-14&pdp_ext_f=%7B%22order%22%3A%22168%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%212.39%210.99%21%21%2116.16%216.71%21%40212e532617837514965934357e6c58%2112000046963609405%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Acbbf39d4%3Bm03_new_user%3A-29895%3BpisId%3A5000000207262948&curPageLogUid=2MQMTnvESN8b&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005008856506094%7C_p_origin_prod%3A
7. https://www.amazon.com/Soldering-Adjustable-Temperature-Multimeter-Desoldering/dp/B09VXQ221K?sr=8-11
8. https://www.alibaba.com/product-detail/Retro-Foldable-Over-ear-Headphones-Wired_1601209006313.html?spm=a2700.prosearch.normal_offer.d_image.93e267afvajTKs&priceId=e2a0d8d91a834ebeae6c6f2182d23f02&priceId=e2a0d8d91a834ebeae6c6f2182d23f02
9. https://www.aliexpress.us/item/3256801334498498.html?spm=a2g0o.productlist.main.1.7b8eQ03rQ03r1T&algo_pvid=aedffa9b-6e19-4d11-afcb-7ab4abf3509e&algo_exp_id=aedffa9b-6e19-4d11-afcb-7ab4abf3509e-0&pdp_ext_f=%7B%22order%22%3A%221000%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.56%211.99%21%21%213.56%211.99%21%402101528c17837481449906811e10c8%2112000033677596105%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Acbbf39d4%3Bm03_new_user%3A-29895%3BpisId%3A5000000210913316&curPageLogUid=OVBC5RW9sUt2&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005001520813250%7C_p_origin_prod%3A
10. https://www.aliexpress.us/item/3256812453298792.html?spm=a2g0o.productlist.main.5.135epVDKpVDKrD&algo_pvid=0ece0587-faca-45fe-ae74-ce0fdc49a8e5&algo_exp_id=0ece0587-faca-45fe-ae74-ce0fdc49a8e5-4&pdp_ext_f=%7B%22order%22%3A%222%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%212.37%212.30%21%21%2115.98%2115.53%21%4021016b6017837514211408378e1e25%2112000058939330286%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Acbbf39d4%3Bm03_new_user%3A-29895&curPageLogUid=3WOHw9kNSGZ4&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005012639613544%7C_p_origin_prod%3A
11. https://www.aliexpress.us/item/3256808837710631.html?spm=a2g0o.productlist.main.19.6be3169d9IfpEl&algo_pvid=60b4bbc2-94ab-41db-91f7-1741716e5e9a&algo_exp_id=60b4bbc2-94ab-41db-91f7-1741716e5e9a-18&pdp_ext_f=%7B%22order%22%3A%2249%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.53%210.99%21%21%213.53%210.99%21%402141115b17837553411484481e35d9%2112000047618726921%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Acbbf39d4%3Bm03_new_user%3A-29895%3BpisId%3A5000000207262948&curPageLogUid=xfWjiIGx5BKH&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009024025383%7C_p_origin_prod%3A
12. https://www.amazon.com/Connector-Solderless-Multicolor-Electronic-Breadboard/dp/B09FPGT7JT?sr=8-7
13. https://www.amazon.com/Patriot-Micro-Flash-Memory-Card/dp/B08KSSXKYR?sr=8-4


Then I designed a rough draft for what the casing may look like
<img width="2509" height="1596" alt="Untitled" src="https://github.com/user-attachments/assets/fa01e07f-0e55-41db-aa26-e02f32b87220" />

Afterwards, I created a diagram to verify that the build would connect
<img width="2509" height="1596" alt="Diagram" src="https://github.com/user-attachments/assets/b566a9aa-205a-4e4a-be8b-0416eab6d251" />

This gave me more clarity to develop a more detailed Design for the case
<img width="2414" height="1596" alt="model" src="https://github.com/user-attachments/assets/afc1ddd6-8df2-4ad6-b374-cab1cd8647da" />

Later in the day i revised my materials list to get rid of out of stock materials
I also finished my bom.csv

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

This allowed me to then create a wiring diagram/schematic hybrid for my project
<img width="1220" height="663" alt="Hybrid Wiring Schematic" src="https://github.com/user-attachments/assets/1ca227be-6414-43a6-bf36-cbe413e19c05" />



After finishing my wiring diagram i read through the wikis and checked the correct pins to use in order to design setup instructions for the build in linux which i includede both in the new setup instructions folder I created and in the new source folder I made.
These setup instructions include:
(OS, driver, and button setup)
(qmmp setup)
(theme setup)

I included all the download links to many of my dependencies in a txt file as well as the readme


My next step was to configure my device to turn on QMMP player automatically always full screen

Lastly for the day I used this tutorial on youtube in order to set up the volume encoder with the help of deepseek to adjust the premade code for my build and the terminal commands in download instructions
https://www.youtube.com/watch?v=4kypUKRMGYk





this left my checklist on my build planning down to the following:

Add screenshot of case 3D model to readme

3d mode production files

3d model case source file

3d model case picture in images


