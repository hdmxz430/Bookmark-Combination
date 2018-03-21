# Bookmark-Combination
Combine Bookmarks from different browsers

The task is to combine the bookmarks from different browsers and the result.

The example input:

Safari bookmarks:

https://mail.google.com/mail/u/0/#inbox

https://www.concur.com/

https://www.sap.com/index.html

https://www.google.com/news/

Chrome bookmarks:

https://mail.google.com/

https://github.com/

https://stackoverflow.com/

https://www.sap.com

Firefox bookmarks:

https://mail.google.com/   

https://github.com/

http://www.sap.com/

https://news.google.com/news/

The output:

[https://mail.google.com/,https://mail.google.com/mail/u/0/#inbox] shorter link should be preferred as first element in list

[https://www.concur.com/]

[https://news.google.com/news/, https://www.google.com/news/]

as opening https://www.google.com/news/ will return an HTTP/2 302 with Location: https://news.google.com/news/

[https://www.sap.com,https://www.sap.com/index.html,http://www.sap.com/] https should be preferred as first element in the list

[https://github.com/]

[https://stackoverflow.com/]

I divided the work into three parts.

## Part1

Combine all the bookmarks into a set. The advantage of a set is that it removes duplicate links.

## Part2

First, I constructed a dictionary to store the url that has the same real url values(address). The key is a string meaning the url's address
the value is a list containing all the url that has the same address.

Use urllib.request.urlopen(url).geturl() to return the real url of the page fetched.

This is important because the same page may have different urls, using geturl can return the same url for different links.

Then, store the real url in the dictionary so that I can check the dictionary first every time I handle a new url and maps to 
that dictionary.

## Part3

Sort the list in the dictionary.

The sorting rule is:

1. url starting with https rank higher

2. url with longer length rank higher

3. Given the same length, urls are sorted in lexicographical order

## Output

['https://mail.google.com/', 'https://mail.google.com/mail/u/0/#inbox']

['https://www.concur.com/']

['https://www.sap.com', 'https://www.sap.com/index.html', 'http://www.sap.com/']

['https://www.google.com/news/', 'https://news.google.com/news/']

['https://github.com/']

['https://stackoverflow.com/']

## Exception

If a url is wrong, the code will raise an exception and tells the users that it will ignore this bookmark.

For example,

The url is 'https://mail.google.con/'

The program would detect that and say this link is invalid, ignore this bookmark: https://mail.google.con/

## Analysis

Suppose we have n bookmarks in total.

Time Complexity: 

gather_bookmarks: O(n)

remove_same_link: O(n)

sort_bookmarks: O(n^2logn)

Space Complexity:

gather_bookmarks: O(n)

remove_same_link: O(n)

sort_bookmarks: O(n)
