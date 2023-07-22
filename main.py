import requests
import csv


def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    final_data = []
    if response.status_code == 200:
        json_data = response.json()['products']
        for data in json_data:
            title = data['title']
            category = data['category']
            price = data['price']
            redPrice = data['redPrice']
            brandName = data['brandName']
            final_data.append({
                            "title":title, "category":category, 
                            "price":price, "redPrice":redPrice, "brandName":brandName
                            })
        
        return final_data
    return None

def saveData(data):
    with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "category", "price", "redPrice", "brandName"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("Scraping and data saving completed successfully.")

        

if __name__ == "__main__":
    url = "https://www2.hm.com/en_in/sale/men/view-all/_jcr_content/main/productlisting_9436.display.json?sort=stock&image-size=small&image=model&offset=72&page-size=1000"
    data = scrape(url)
    if data: 
        saveData(data)
    else: 
        print("Url not found!")

    
