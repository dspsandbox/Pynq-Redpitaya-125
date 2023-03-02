# PYNQ for Redpitaya-125-14


---

ℹ️ For a tutorial on FPGA programming with Redpitaya-125-14 and PYNQ see [FPGA Notes for Scientists](https://github.com/dspsandbox/FPGA-Notes-for-Scientists).

---
This repository describes the generation of a PYNQ image for the Redpitaya STEMlab 125-14 board. The device tree has been simplified and the supported MIO peripherals are:
* SD 0
* UART 0
* ENET 0 (static MAC address, read from i2c EEPROM during boot)
* USB 0


## Ready-to-use downloads, links and base design

* [Pynq-Redpitaya-125-14-3.0.1.img](https://drive.google.com/file/d/129EsJnPIXDf8AoeYgjwcfgi8bE3UVRis/view?usp=sharing)
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
We follow the steps outlined under [PYNQ SD card](https://pynq.readthedocs.io/en/v3.0.0/pynq_sd_card.html):

* Install a virtual machine running Ubuntu **18_04_4 LTS** with more than 150 GB of storage space. Do not update Ubuntu since this will roll the version and make it incompatible with the Xilinx tools below. 

* Clone the PYNQ repository (for this build we used **v3.0.1**):
```bash
git clone https://github.com/Xilinx/PYNQ
```
* Install dependencies using the following script.
```bash
source <PYNQ repository>/sdbuild/scripts/setup_host.sh
```
* Install the Xilinx tools (for this build we used **v2022.1**): 
   * Vitis (which includes Vivado) 
   * Petalinux
   * Go for lunch! This will take a few hours...

* Download the prebuilt board-agnostic (PYNQ rootfs arm v3.0.1) image from [Pynq Development Boards ](http://www.pynq.io/board.html/) and unzip it.
* Download the PYNQ distribution tarball (pynq-3.0.1.tar.gz) from the [PYNQ release repository](https://github.com/Xilinx/PYNQ/releases). You will find the distribution tarball under a drop-down called *Assets*.
* Place both files into *<PYNQ repository>/sdbuild/prebuilt/*

### Prepare build
* Clone this repository:
```bash
git clone https://github.com/dspsandbox/Pynq-Redpitaya-125
```
* Copy the provided board directory *\<this repository\>/Pynq/boards/Pynq-Redpitaya-125-14* to *\<PYNQ repository\>/boards*. 


### Build PYNQ 
* Open a terminal and run the settings files for Vitis and Petalinux:
```bash
source <path-to-vivado>/2022.1/settings64.sh
source <path-to-vitis>2022.1/settings64.sh
source <path-to-petalinux>/2022.1/tool/settings.sh
```

* Navigate to 
```bash
cd <PYNQ repository>/sdbuild
```
* Run the makefile (your password will be required a couple of times)
```bash
make BOARDS=Pynq-Redpitaya-125-14
```
* The generated PYNQ image will be located within *\<PYNQ repository\>/sdbuild/output/Pynq-Redpitaya-125-14-3.0.1.img*



