import json
import random
import os

def generate_product_data(num_products,save=False):
    directory="./test_data/"
    file_name="products_"+ str(num_products) +".json"
    
    #check if file exist
    saved_products=search_file_and_load(directory,file_name)
    if saved_products:
        return saved_products
    products = []
    for i in range(num_products):
        product = {
            "name": f"Product {i+1}",
            "image": f"product{i+1}.jpg",
            "variants": []
        }
        n=random.randint(1, 50)#random number of variants
        for j in range(n): 
            variant = {
                "sku": f"variant{j+1}",
                "name": f"Variant {j+1}",
                "price": round(random.uniform(1.0, 20.0), 2),
                "details": "details...."
            }
            product["variants"].append(variant)
        products.append(product)
        json_request = json.dumps(products)
        if not os.path.exists(directory):
            os.makedirs(directory)
    if save:        
        
        with open(directory + file_name, "w") as outfile:
            outfile.write(json_request)
       
    return products    
         

def search_file_and_load(directory, filename):
   
    for root, dirs, files in os.walk(directory):
       
        if filename in files:
          
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:
                
                json_content = json.load(file)
           
            return json_content
    
    return None

  


