import sys
import os
import logging
import time
import traceback

import epd_control
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)


try:
	epd = epd_control.EPD()
	epd.init()
	epd.Clear()

	font18 = ImageFont.truetype('Font.ttc', 18)
	font24 = ImageFont.truetype('Font.ttc', 24)

	# Drawing on the Horizontal image
	logging.info("1.Drawing on the Horizontal image...")
	Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
	Other = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
	draw_Himage = ImageDraw.Draw(Himage)
	draw_other = ImageDraw.Draw(Other)
	draw_Himage.text((10, 0), 'hello world', font = font24, fill = 0)
	draw_Himage.text((10, 20), '7.5inch e-Paper', font = font24, fill = 0)
	draw_Himage.text((150, 0), u'微雪电子', font = font24, fill = 0)
	draw_other.line((20, 50, 70, 100), fill = 0)
	draw_other.line((70, 50, 20, 100), fill = 0)
	draw_other.rectangle((20, 50, 70, 100), outline = 0)
	draw_other.line((165, 50, 165, 100), fill = 0)
	draw_Himage.line((140, 75, 190, 75), fill = 0)
	draw_Himage.arc((140, 50, 190, 100), 0, 360, fill = 0)
	draw_Himage.rectangle((80, 50, 130, 100), fill = 0)
	draw_Himage.chord((200, 50, 250, 100), 0, 360, fill = 0)
	epd.display(epd.getbuffer(Himage),epd.getbuffer(Other))
	time.sleep(2)

	# Drawing on the Vertical image
	logging.info("2.Drawing on the Vertical image...")
	Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
	Limage_Other = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
	draw_Himage = ImageDraw.Draw(Limage)
	draw_Himage_Other = ImageDraw.Draw(Limage_Other)
	draw_Himage.text((2, 0), 'hello world', font = font18, fill = 0)
	draw_Himage.text((2, 20), '7.5inch epd', font = font18, fill = 0)
	draw_Himage_Other.text((20, 50), u'微雪电子', font = font18, fill = 0)
	draw_Himage_Other.line((10, 90, 60, 140), fill = 0)
	draw_Himage_Other.line((60, 90, 10, 140), fill = 0)
	draw_Himage_Other.rectangle((10, 90, 60, 140), outline = 0)
	draw_Himage_Other.line((95, 90, 95, 140), fill = 0)
	draw_Himage.line((70, 115, 120, 115), fill = 0)
	draw_Himage.arc((70, 90, 120, 140), 0, 360, fill = 0)
	draw_Himage.rectangle((10, 150, 60, 200), fill = 0)
	draw_Himage.chord((70, 150, 120, 200), 0, 360, fill = 0)
	epd.display(epd.getbuffer(Limage), epd.getbuffer(Limage_Other))
	time.sleep(2)

	logging.info("Clear...")
	epd.init()
	epd.Clear()

	logging.info("Goto Sleep...")
	epd.sleep()
	time.sleep(3)

	epd.Dev_exit()

except IOError as e:
		logging.error(e)

except KeyboardInterrupt:
		logging.info("ctrl + c:")
		epd_control.epdconfig.module_exit()
		exit()
