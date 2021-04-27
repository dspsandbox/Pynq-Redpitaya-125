# PYNQ for Redpitaya-125-14

This repository describes the generation of a PYNQ image for the Redpitaya STEMlab 125-14 board. The device tree has been simplified and the supported external interfaces are:

* Ethernet
* USB
* UART


## Ready-to-use downloads, links and base design

* [Pynq-Redpitaya-125-14-2.6.0.img](https://drive.google.com/file/d/1YY4HYoDWa3E1ZVyxrV7naTFVoDieKrwm/view?usp=sharing)
* [Instructions on writing the SD card image](https://pynq.readthedocs.io/en/v2.6.1/appendix.html#writing-the-sd-card-image)
* [Getting started with PYNQ](https://pynq.readthedocs.io/en/v2.0/getting_started.html)
* [Vivado Redpitaya-125-14 board files](https://github.com/dspsandbox/Pynq-Redpitaya-125/tree/master/Vivado/board_files)
* [Redpitaya constraint file (.xdc)](https://github.com/RedPitaya/RedPitaya/blob/master/fpga/sdc/red_pitaya.xdc)
* Base design (the corresponding overlay is included within the build image):
<img src="/Doc/base_bd.png"/>

* Controlling the base design from a PYNQ Jupyer Notebook:

```python
import time
import pynq
ol = pynq.Overlay("base.bit")

for i in range(8):
    ol.led_ctrl.channel1.write(val=(1<<i), mask=0xff)
    time.sleep(0.5)
```
<img src="/Doc/running_led.gif" width="400"/>


## Build process 
### Get the environment ready
In progress...
