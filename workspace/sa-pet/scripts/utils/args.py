import sys

def get_args_dict():
    args_dict = {}
    for arg in sys.argv[1:]:
        key, value = arg.split('=')
        args_dict[key] = value
    return args_dict


# 测试
def __test__():
    args_dict = get_args_dict()
    print(args_dict)

if __name__ == '__main__':
    __test__()