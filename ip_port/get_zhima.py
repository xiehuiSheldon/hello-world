import random

def get_zhima_proxy(filename):
    zhima_proxy_list = []
    with open(filename, 'r') as fp:
        for line in fp:
            zhima_proxy_list.append(line.strip())
    return zhima_proxy_list
    
if __name__ == '__main__':
    zhima_proxy_list = get_zhima_proxy('zhima.txt')
    print(random.choice(zhima_proxy_list))