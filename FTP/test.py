from urllib.parse import urlparse
def main():
    response = '227 Entering Passive Mode (54,235,102,179,141,109).'
    start = response.find('(')
    end = response.find(')')
    ip_num = list(map(int, response[start+1:end].split(',')))
    ip_address = '.'.join(map(str, ip_num[:4]))
    port = (int(ip_num[4]) << 8) + int(ip_num[5])
    print(ip_num)
    print(ip_address)
    print(port)

    url = 'ftp://lyuyun:293fh@3700.network/dir/qqt'
    print(parse_url(url))


def parse_url(url):
    # If the scheme is 'ftp' and there's no dot in the netloc, 
    # consider netloc as part of the path
    parsed_url = urlparse(url)
    if parsed_url.scheme == 'ftp' and '.' not in parsed_url.netloc:
        path = parsed_url.netloc + parsed_url.path
    else:
        path = parsed_url.path
    # Remove the leading '/' from the path
    return path[1:] if path.startswith('/') else path
main()

