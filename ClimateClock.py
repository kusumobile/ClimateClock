#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import datetime


class RunText(SampleBase):

    xDay = datetime.datetime.strptime('2028-1-1 00:00:00','%Y-%m-%d %H:%M:%S')

    yDay = datetime.datetime.now()

    remaining = "残り"

    def clock():
      global remaining
      zDay = xDay - yDay

      while True:
        day  = str(int(zDay.days))
        hour = str(int(zDay.seconds/3600))
        min  = str(int((zDay.seconds/60)%60))
        sec  = str(int((zDay.seconds)%60))
        remaining = "残り"+ day + "日" + hour + "時間" + min + "分" + sec + "秒"
        print(remaining)
        zDay -= datetime.timedelta(seconds=1)
        time.sleep(1)

    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        clock()
        my_text = remaining

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.01)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
