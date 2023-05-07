
import argparse
import sys
from SeleniumScrapper import Scrapper

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Webscrapper that scraps some text')
    
    parser.add_argument("-u", "--url", action="store",
                        dest="url", 
                        help="Url to start scrapping")
    parser.add_argument("-xb", "--Xpathbutton", action="store",
                        dest="Xpathbutton",
                        help="Xpath of next button")
    parser.add_argument("-xc", "--Xpathcontent", action="store",
                    dest="Xpathcontent",
                    help="Xpath of content you want to store")
    
    parser.add_argument("-t", "--title", action="store",
                        dest="title", default="Download.txt",
                        help="Name of your txt file")
    parser.add_argument("-a", "--ads", action="store",
                        dest="ads", default="AdSnippets.txt",
                        help="Name of your txt file with ad lines separated by ; ")
    
    parser.add_argument("-f", "--first", action="store",
                        dest="first", default=1, type=int,
                        help="What is the chapter you start on")

    parser.add_argument("-l", "--last", action="store",
                        dest="last", default=9999, type=int,
                        help="What is last chapter you want to end on")
    parser.add_argument("-he", "--headless",action='store_const',
                        dest="headless", default=True, const=False,
                        help="Run headless or not")
    sys.argv = [ 'main.py', '-u', 
     'https://www.scribblehub.com/series/485634/iris-and-me/',
      '-xb', '//*[@class="btn-wi btn-next"]', '-xc', '//*[@id="chp_raw"]',
       '-t', 'C:\\Users\\Woda\\Desktop\\New Novels\\rename\\iris-and-me.txt','-a',
       'C:\\Users\\Woda\\Desktop\\Python_Projects\\SeleniumScrapper\\AdSnippets.txt','-l', '999','-he']
    args = parser.parse_args()
    if not args.url and not args.Xpathbutton and not args.Xpathcontent:
        print("Something went wrong!")
        print(parser.print_help())
        exit()
driver=Scrapper.Setup(Headless=args.headless)
Scrapper.Scrap(driver,args.url,args.Xpathbutton,args.Xpathcontent,
        chapter=args.first,endchapter=args.last,title=args.title,AdFilePath=args.ads)


    
