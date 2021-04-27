# PYNQ for Redpitaya-125-14

This repository describes the generation of a PYNQ image for the Redpitaya STEMlab 125-14 board, with the intend to provide a simple FPGA development environment for this open-source DSP platform. 
The device tree has been simplified and the supported external interfaces are:

* Ethernet
* USB
* UART


## Ready-to-use downloads & links

* [Pynq-Redpitaya-125-14-2.6.0.img](https://drive.google.com/file/d/1YY4HYoDWa3E1ZVyxrV7naTFVoDieKrwm/view?usp=sharing)
* [Instructions on writing the SD card image](https://pynq.readthedocs.io/en/v2.6.1/appendix.html#writing-the-sd-card-image)
* [Vivado Redpitaya-125-14 board files](https://github.com/dspsandbox/Pynq-Redpitaya-125/tree/master/Vivado/board_files)
* Base design:
<img src="/Doc/base_bd.png"/>

* Running led example:

```python
import time
import pynq
ol = pynq.Overlay("base.bit")

for i in range(8):
    ol.led_ctrl.channel1.write(val=(1<<i), mask=0xff)
    time.sleep(0.5)
```
<img src="/Doc/running_led.gif"/>


## Build process (in progress...)
### Get the environment ready
