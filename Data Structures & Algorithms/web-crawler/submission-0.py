# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = self.get_hostname(startUrl)
        res = set()

        def dfs(cur):
            if cur in res:
                return
            res.add(cur)

            for url in htmlParser.getUrls(cur):
                if hostname != self.get_hostname(url) or url in res:
                    continue
                dfs(url)
        
        dfs(startUrl)
        return list(res)

    
    def get_hostname(self, url):
        return url.split('/')[2]