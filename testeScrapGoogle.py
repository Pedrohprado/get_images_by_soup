import requests
from bs4 import BeautifulSoup


def google_images_download(directory, search, num_of_img):
    search_mod = search.upper()
    search_mod = search_mod.split()

    url1 = f'https://www.google.com/search?q={search}&hl=pt-BR&tbm=isch&source=hp&biw=1366&bih=649&ei=8diRZMKMPIaL5OUPxaizkAw&iflsig=AOEireoAAAAAZJHnAvGuJqBENBAUrfEWlOFshTBNcY_3&ved=0ahUKEwiCycmkp9L_AhWGBbkGHUXUDMIQ4dUDCAc&uact=5&oq=m&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQNQgqcBWIKnAWCfrAFoAHAAeACAAW6IAW6SAQMwLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAA&sclient=img'

    i = 0
    links_list = []
    repeat_img = []

    response = requests.get(url1)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table', attrs={'class': 'IkMU6e'})

    for links in table:
        links_list.append(links.a.get('href'))

    links_list = [sites[7:sites.index('&')] for sites in links_list]

    for link in links_list:
        if i == num_of_img:
            break
        try:
            url = link
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            images = soup.find_all('img')

            for image in images:  # write bit 'wb'
                if i == num_of_img:
                    break
                if '.svg' in image.get('src') or image.get('src') == None:
                    pass
                if image.get('src') in repeat_img:
                    pass
                search_comp = [i in image.get('src').upper() for i in search_mod]
                if search_comp.count(True) == len(search_comp) and 'http' in image.get('src'):
                    with open(f'{directory}/{search.lower()}_{i}.png', 'wb') as f:
                        img_response = requests.get(image.get('src'))

                        if img_response.status_code == 200:  # sucess
                            if i == num_of_img:
                                break
                            else:
                                print(image.get('src'), '-', i)
                                repeat_img.append(image.get('src'))
                                f.write(img_response.content)
                                i += 1
                        else:
                            continue
        except:
            pass

    page = 20
    if i < num_of_img:

        while True:
            links_list = []
            urln = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&tbm=isch&ei=78xeX5PTGc_Z5OUPrsyA0A0&start={page}&sa=N'

            response = requests.get(urln)
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find_all('table', attrs={'class': 'IkMU6e'})

            for links in table:
                links_list.append(links.a.get('href'))

            links_list = [sites[7:sites.index('&')] for sites in links_list]

            for link in links_list:
                if i == num_of_img:
                    break
                try:
                    url = link
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    images = soup.find_all('img')

                    for image in images:  # write bit 'wb'
                        if i == num_of_img:
                            break
                        if '.svg' in image.get('src') or image.get('src') == None:
                            pass
                        if image.get('src') in repeat_img:
                            pass
                        search_comp = [i in image.get('src').upper() for i in search_mod]
                        if search_comp.count(True) == len(search_comp) and 'http' in image.get('src'):
                            with open(f'{directory}/{search.lower()}_{i}.png', 'wb') as f:
                                img_response = requests.get(image.get('src'))

                                if img_response.status_code == 200:  # sucess
                                    if i == num_of_img:
                                        break
                                    else:
                                        print(image.get('src'), '-', i)
                                        repeat_img.append(image.get('src'))
                                        f.write(img_response.content)
                                        i += 1
                                else:
                                    continue
                except:
                    pass

            if i < num_of_img:
                page += 20
            else:
                break
    print('')
    print(f'{i} images were downloaded')
    print('')


if __name__ == '__main__':
    while True:
        directory = str(input('Directory: '))
        search = str(input('What images do you want to download? '))
        num_of_img = int(input('How many images do you want to download? '))
        
        google_images_download(directory, search, num_of_img)