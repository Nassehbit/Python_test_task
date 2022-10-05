
from scripts.extra_script import extra_main
from scripts.root_script import root_main
from scripts.segmentation_script import seg_main
from scripts.super_resolution_script import sup_main
def main():
    extra_main()
    root_main()
    sup_main()
    seg_main()

    print('SUCCESSFULY CREATED OUTPUT FOLDERS AND FILES')

if __name__ == "__main__":
    main()