# PYNQ for Redpitaya-125-14

This repository describes the generation of a PYNQ image for the Redpitaya STEMlab 125-14 board. The device tree has been simplified and the supported MIO peripherals are:
* SD 0
* UART 0
* ENET 0
* USB 0


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
We follow the steps outlined under [PYNQ SD card](https://pynq.readthedocs.io/en/v2.6.1/pynq_sd_card.html):

* Install a virtual machine running Ubuntu **18_04_4 LTS** with more than 150 GB of storage space. Do not update Ubuntu since this will roll the version and make it incompatible with the Xilinx tools below. 

* Clone the PYNQ repository (for this build we used **v2.6**):
```bash
git clone https://github.com/Xilinx/PYNQ
```
* Install dependencies using the following script.
```bash
source <PYNQ repository>/sdbuild/scripts/setup_host.sh
```
* Install the Xilinx tools (for this build we used **v2020.1**): 
   * Vitis (which includes Vivado) 
   * Petalinux
   * Go for lunch! This will take a few hours...

* Download the prebuilt board-agnostic (PYNQ rootfs arm v2.6) image from [Pynq Development Boards ](http://www.pynq.io/board.html/) and unzip it.
* Download the PYNQ distribution tarball (Pynq-2.6.0.tar.gz) from the [PYNQ release repository](https://github.com/Xilinx/PYNQ/releases). You will find the distribution tarball within the *WFH Release* section under a drop-down called *Assets*.

### Prepare build
* Clone this repository:
```bash
git clone https://github.com/dspsandbox/Pynq-Redpitaya-125
```
* Copy the provided board directory *\<this repository\>/Pynq/boards/Pynq-Redpitaya-125-14* to *\<PYNQ repository\>/boards*. 

* Modify the FPGA makefile under *\<PYNQ repository\>/sdbuild/Makefile*:
   * Locate on line 162 the command *petalinux-config --silentconfig -p $$(PL_PROJ_$1)*.
   * Add above it a command to copy the *petalinux_project* located in our board directory. This will include our device tree (*system-user.dtsi*) into the PYNQ build process. The modified makfile reads:
```bash
# ...
echo 'CONFIG_zocl=y' >> $$(PL_ROOTFS_CONFIG_$1)
echo 'CONFIG_opencl-headers-dev=y' >> $$(PL_ROOTFS_CONFIG_$1)
echo 'CONFIG_opencl-clhpp-dev=y' >> $$(PL_ROOTFS_CONFIG_$1)
cp -a $$(BOARDDIR_$1)/petalinux_project/. $$(PL_PROJ_$1)  # ADD THIS LINE !!!
petalinux-config --silentconfig -p $$(PL_PROJ_$1) 
# ...
```

### Build PYNQ 
* Open a terminal and run the settings files for Vitis and Petalinux:
```bash
source <path-to-vitis>/Vitis/2020.1/settings64.sh
source <path-to-petalinux>/petalinux-2020.1-final/settings.sh
petalinux-util --webtalk off
```

* Navigate to 
```bash
cd <PYNQ repository>/sdbuild
```
* Issue a dummy *sudo* call:  
```bash
sudo echo hello
```
* Run the makefile
```bash
make PREBUILT=<absolute path to unzipped board-agnostic perbuilt image (.img)> PYNQ_DIST=<absolute path to PYNQ tarball (.tar.gz)> BOARDS=Pynq-Redpitaya-125-14
```
* The generated PYNQ image will be located within *\<PYNQ repository\>/sdbuild/output/Pynq-Redpitaya-125-14-2.6.0.img*



