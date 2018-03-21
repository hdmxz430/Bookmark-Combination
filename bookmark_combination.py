import urllib.request as request
import ssl
import functools
from urllib import error

context = ssl._create_unverified_context()


def gather_bookmarks():
    safari_bookmarks = ['https://mail.google.com/mail/u/0/#inbox', 'https://www.concur.com/', 'https://www.sap.com/index.html', 'https://www.google.com/news/']
    chrome_bookmarks = ['https://mail.google.com/', 'https://github.com/', 'https://stackoverflow.com/', 'https://www.sap.com']
    firefox_bookmarks = ['https://mail.google.com/', 'https://github.com/', 'http://www.sap.com/', 'https://news.google.com/news/']
    all_bookmarks = safari_bookmarks + chrome_bookmarks + firefox_bookmarks
    return all_bookmarks


def remove_duplicate(all_bookmarks):
    output_bookmarks = {}
    for bookmark in all_bookmarks:
        #print(bookmark)
        try:
            result = request.urlopen(bookmark, context = context)
        except error.URLError as e:
            print('this link is invalid, ignore this bookmark:', bookmark) 
            continue
        name = result.geturl()
        if name in output_bookmarks:
            if bookmark not in output_bookmarks[name]:
                output_bookmarks[name].append(bookmark)
        else:
            output_bookmarks[name] = []
            output_bookmarks[name].append(bookmark)
    return output_bookmarks

def sort_bookmarks(output_bookmarks):
    output_bookmarks_list = []
    for key in output_bookmarks:
        bookmarks = output_bookmarks[key]
        #print(bookmarks)
        sorted_bookmarks = sorted(bookmarks, key = functools.cmp_to_key(sort_func))
        #print(sorted_bookmarks)
        output_bookmarks_list.append(sorted_bookmarks)
    return output_bookmarks_list
    

def sort_func(url1, url2):
    url1_http = url1[0:5]
    url2_http = url2[0:5]
    if url1_http == 'https' and url2_http == 'http:':
        return -1
    if url1_http == 'http:' and url2_http == 'https':
        return 1
    
    if len(url1) > len(url2):
        return 1
    elif len(url2) > len(url1):
        return -1
    else:
        if url1 > url2:
            return 1
        else:
            return -1

if __name__ == '__main__':
    gathered_bookmarks = gather_bookmarks()
    removed_duplicate_bookmarks = remove_duplicate(gathered_bookmarks)
    output_bookmarks = sort_bookmarks(removed_duplicate_bookmarks)
    for bookmark_list in output_bookmarks:
        print(bookmark_list)
