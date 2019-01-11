# Auto Image Inverter

Inverts a picture (and each other in the folder and it's subfolder) if there is more black than white pixels. I scripted this for my bachelorthesis where I've got plenty of diagrams crafted in a black theme, which don't look pretty well when printed.

# How To Use

The script can be controlled by command line arguments. It needs to be placed in the top folder where the images are located.
The following shows the help:


usage: autoImageInverter.py [-h] [--filter FILTER] [--prefix PREFIX]
                            [--precision PRECISION]
                            [--skipConfirm SKIPCONFIRM]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  --filter FILTER       Filter applying when searching for images
  --prefix PREFIX       Prefix to indicate converted files
  --precision PRECISION
                        Only process every precision th line
  --skipConfirm SKIPCONFIRM
                        Skip confirmation for auto processing. Pass Y as value