from wkcp.utils import extract_img


def handle(args):
    filelines = list()

    with open(args.file[0], 'r') as fp:
        filelines = fp.readlines()

    lines_with_images = list()
    for i in range(len(filelines)):
        image = extract_img(filelines[i])
        if image:
            lines_with_images.append(i)
            print(image)
