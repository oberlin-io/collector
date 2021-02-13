import yaml


def get():

    with open('config.yaml') as f:

        return yaml.safe_load(f.read())


if __name__ == '__main__':
    print(get())
