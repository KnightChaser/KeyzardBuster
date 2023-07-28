# KeyzardBuster (For `blog.naver.com` users)

1. Execute `get_blog_post_urls.py` to extract every URL of posts in your blog.
2. After step `1`, execute `auto_register.py` to automatically register your blog post to kzd's Google registering service.

This code may be unstable because it hasn't been tested enough. However, it seems to be operating normally in usual usage. Please feel free to leave any issues whenever you find something to be fixed or improved.


#### Future improvements (probably)
`auto_register.py`: My method is based on the assumption that every registering process would be okay(not blocked by the security system) unless this script works so fast that the administrator would consider this spam. However, it'd be better to handle the alert message indirectly - by checking the result response after registering. Officially, the `Selenium` package in Python3 doesn't support getting and utilizing responses from websites like `requests`. Based on my simple research, I checked every process can be conducted statically. So I'd like to switch my method to use `requests` in the future.
