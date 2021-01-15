'''
    === Instagram Scraper ===
    version: 0.1
    
    status: chưa viết mấy trường hợp exception và kiểm tra input
'''

import requests as r
import os

# init color text
red_clr = "\033[91m"
blue_clr = "\033[96m"
green_clr = "\033[92m"
orage_clr = "\033[33m"
lightgreen_clr = "\033[92m"
lightblue_clr = "\033[94m"
reset_clr = "\033[00m"

def print_banner():
    """
    Hàm này dùng để in banner cho chương trình
    :return: void
    """
    print(blue_clr + " .___         _________                                         " + reset_clr)
    print(blue_clr + " |   | ____  /   _____/ ________________  ______   ___________  " + reset_clr)
    print(blue_clr + " |   |/    \\ \\_____  \\_/ ___\\_  __ \\__  \\ \\____ \\_/ __ \\_  __ \\ " + reset_clr)
    print(blue_clr + " |   |   |  \\/        \\  \\___|  | \\// __ \\|  |_> >  ___/|  | \\/ " + reset_clr)
    print(blue_clr + " |___|___|  /_______  /\\___  >__|  (____  /   __/ \\___  >__|    " + reset_clr)
    print(blue_clr + "          \\/        \\/     \\/           \\/|__|        \\/        " + reset_clr)
    print()
    print(green_clr + "  Version: 0.1" + reset_clr)

def print_menu():
    """
    Hàm này dùng để in menu lựa chọn
    :return: void
    """
    print()
    print(" -- " + green_clr + "MENU" + reset_clr + " -----------------------------------------")
    print(" | [1] Tìm kiếm username theo mức độ liên quan   |")
    print(" | [2] Tìm thông tin tài khoản                   |")
    print(" | [3] Tải xuống tất cả hình của một tài khoản   |")
    print(" |                                               |")
    print(" | [0] Thoát                                     |")
    print(" -------------------------------------------------")
    print()

def find_username(search_info):
    """
    Hàm này dùng để tìm kiếm username theo mức độ liên quan
    Response Time: ~200ms
    :param search_info: string
    :return: list(string)
    """
    header = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "cache-control": "max-age=0", "cookie": "ig_did=201CD758-3C2E-464B-BEE3-3A171D189F99; mid=XfnpKQAEAAFPnJGxXm4uNHvKE2UV; fbm_124024574287414=base_domain=.instagram.com; csrftoken=8svP6VBv8Rt2jKc8JFN5m0uCdzxuLeTc; ds_user_id=27949455512; sessionid=27949455512%3ABPkrtkF1q7Ow4v%3A22; shbid=6232; shbts=1606061923.7904177; rur=FTW;", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    response = r.get("https://www.instagram.com/web/search/topsearch/?context=user&count=0&query=" + search_info, headers = header)
    data = response.json()
    return [i['user']['username'] for i in data['users']]

def find_id(username):
    """
    Hàm này dùng để tìm id theo username
    Response Time: ~200ms
    :param username: string
    :return: string 
    """
    header = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "cache-control": "max-age=0", "cookie": "ig_did=201CD758-3C2E-464B-BEE3-3A171D189F99; mid=XfnpKQAEAAFPnJGxXm4uNHvKE2UV; fbm_124024574287414=base_domain=.instagram.com; csrftoken=8svP6VBv8Rt2jKc8JFN5m0uCdzxuLeTc; ds_user_id=27949455512; sessionid=27949455512%3ABPkrtkF1q7Ow4v%3A22; shbid=6232; shbts=1606061923.7904177; rur=FTW;", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    response = r.get("https://www.instagram.com/web/search/topsearch/?context=user&count=0&query=" + username, headers = header)
    data = response.json()
    return data['users'][0]['user']['pk']

def find_account_info(username):
    """
    Hàm này dùng để tìm id theo username
    Response Time: ~200ms
    Return's data: 
    {
        id : ...,
        username : ...,
        full_name: ...,

    }
    :param username: string
    :return: string 
    """
    header = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "cache-control": "max-age=0", "cookie": "ig_did=201CD758-3C2E-464B-BEE3-3A171D189F99; mid=XfnpKQAEAAFPnJGxXm4uNHvKE2UV; fbm_124024574287414=base_domain=.instagram.com; csrftoken=8svP6VBv8Rt2jKc8JFN5m0uCdzxuLeTc; ds_user_id=27949455512; sessionid=27949455512%3ABPkrtkF1q7Ow4v%3A22; shbid=6232; shbts=1606061923.7904177; rur=FTW;", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    response = r.get("https://www.instagram.com/web/search/topsearch/?context=user&count=0&query=" + username, headers = header)
    data = response.json()
    return data['users'][0]['user']

def scraper(id, username=""):
    """
    Hàm này dùng để cào thông tin theo id (tạo thư mục theo id và tải file hình xuống)
    :param id: string
    :return: void
    """
    current_path = os.getcwd()
    folder_name = username + "-" + id
    try:
        os.mkdir(current_path + "\\" + folder_name + "\\")
    except:
        pass

    header = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cookie": 'ig_did=201CD758-3C2E-464B-BEE3-3A171D189F99; mid=XfnpKQAEAAFPnJGxXm4uNHvKE2UV; fbm_124024574287414=base_domain=.instagram.com; csrftoken=8svP6VBv8Rt2jKc8JFN5m0uCdzxuLeTc; ds_user_id=27949455512; sessionid=27949455512%3ABPkrtkF1q7Ow4v%3A22; shbid=6232; shbts=1610601542.4573383; rur=FTW; urlgen="{\"171.239.168.4\": 7552}:1l0J4f:fM_rkEy7pUjL9DCMivYdFUdDows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "x-csrftoken": "8svP6VBv8Rt2jKc8JFN5m0uCdzxuLeTc",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR3V2lyYjhr1HaEfF78GZYRruFVzJsZ7LvejFjUBlKFtJXI0",
        "x-requested-with": "XMLHttpRequest"
    }
    linkStart = 'https://www.instagram.com/graphql/query/?query_hash=003056d32c2554def87228bc3fd9668a&variables={"id":"'+id+'","first":12,"after":"QVFCSmJaTWxHbTZ0TzJCdGlnMGRIRmM5WjE0cTlfamlST1BaN2I5V3U4S3hMS3VJdGoxUzd0ZlBOdVBQM1F1WDRtaHJZZXc5WWYwbXZObHRKMGFxM3llUA=="}'
    print(linkStart)
    nextLink= ''
    # print( r.get(linkStart))
    firstres = r.get(linkStart, headers = header).json()
    check = firstres['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
    end = firstres['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']

    total_files = 0
    link = []
    while check != False:
        nextLink = 'https://www.instagram.com/graphql/query/?query_hash=003056d32c2554def87228bc3fd9668a&variables={"id":"'+id+'","first":12,"after":"'+end+'"}'
        res = r.get(nextLink, headers = header).json()
        edges = res['data']['user']['edge_owner_to_timeline_media']['edges']
        for e in edges:
            is_video = e['node']['is_video']
            if is_video is False:
                link.append(e['node']['display_url'])
            if "edge_sidecar_to_children" in e['node']:
                ne = e['node']['edge_sidecar_to_children']['edges']
                for nee in ne:
                    is_video = nee['node']['is_video']
                    if is_video is False:
                        link.append(nee['node']['display_url'])
        end = res['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        check = res['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
        # print(len(link))
        for l in link:
            file_name = str(l).split('/')[-1].split('?')[0]
            with open(folder_name + '/' + file_name, "wb") as file:
                    response = r.get(l)
                    total_files += 1
                    print(total_files)
                    file.write(response.content)
                    file.close()
        link = []
        if check == False:
            break

    print("Tải xuống thành công!!!")
    print("Tổng cộng:", total_files, "files")

def option_1():
    """
    Hàm này dùng để thực hiện option 1 trên menu
    :return: void
    """
    search_info = input("Search's content: ")
    ls_username = find_username(search_info)

    stt = 1
    for i in ls_username:
        print("[", stt, "]", i)
        stt += 1
    print("Total:", len(ls_username))

def option_2():
    """
    Hàm này dùng để in thông tin của một account
    :return: void
    """
    username = input("Username: ")
    account_info = find_account_info(username)
    for i in account_info:
        print(i, ": ", account_info[i], sep = "")


def option_3():
    """
    Hàm này dùng để tải xuống tất cả hình của một user
    :return: void
    """
    username = input("Username: ")
    scraper(find_id(username), username)


if __name__ == "__main__":
    print_banner()
    print_menu()
    option = -1

    while option != '0':
        option = input(lightblue_clr + "Option: " + reset_clr)
        
        if option == '1':
            option_1()
        elif option == '2':
            option_2()
        elif option == '3':
            option_3()
        elif option == '0':
            print()
            print(blue_clr + "Cảm ơn bạn đã sử dụng chương trình" + reset_clr)
            print(red_clr + "\nThoát\n" + reset_clr)
        else:
            print(red_clr + "\nNhập Sai\n" + reset_clr)
        