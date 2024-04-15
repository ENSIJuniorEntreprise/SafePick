from django.http import JsonResponse
import pymongo
from bson import ObjectId  # Import ObjectId from bson module
from django.conf import settings
from django.http import JsonResponse
from .models import ProductF,ProductC
import json
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

def get_productF_field(request, product_code, field_name):
    my_client = pymongo.MongoClient(settings.DB_NAME)
    dbname = my_client['Safepick']
    collection_name = dbname["food"]

    # Find the product with the specified code
    product = collection_name.find_one({'code': product_code})

    if product:
        # Check if the field exists in the product document
        if field_name in product:
            field_value = product[field_name]
            return JsonResponse({field_name: field_value})
        else:
            return JsonResponse({'error': 'Field does not exist'})
    else:
        return JsonResponse({'error': 'Product not found'})
    
    

def foodApi(request, id=0):
    if request.method == 'GET':
        my_client = pymongo.MongoClient(settings.DB_NAME)
        dbname = my_client['Safepick']
        collection_name = dbname["food"]
        med_details = list(collection_name.find({}))  # Convert Cursor to list of dictionaries
        
        # Convert ObjectId instances to strings
        for item in med_details:
            item['_id'] = str(item['_id'])
        
        return JsonResponse(med_details, safe=False)

def cosmeticApi(request, id=0):
    if request.method == 'GET':
        my_client = pymongo.MongoClient(settings.DB_NAME)
        dbname = my_client['Safepick']
        collection_name = dbname["cosmetics"]
        med_details = list(collection_name.find({}))  # Convert Cursor to list of dictionaries
        
        # Convert ObjectId instances to strings
        for item in med_details:
            item['_id'] = str(item['_id'])
        
        return JsonResponse(med_details, safe=False)
    
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
def Alternatives(request, product_id, collection_name):
    if request.method == 'GET':
        try:
            # Connect to the MongoDB database
            my_client = pymongo.MongoClient(settings.DB_NAME)
            dbname = my_client['Safepick']
            collection = dbname[collection_name]

            # Retrieve the specific product
            specific_product = collection.find_one({'_id': ObjectId(product_id)})

            if specific_product:
                # Retrieve the current product's score
                current_product_score = specific_product.get('score', 0)

                # Try retrieving the specific category first
                specific_category = specific_product.get('pnns_groups_1')

                # If specific category doesn't exist or is null, fallback to pnns_groups_2
                if not specific_category:
                    specific_category = specific_product.get('pnns_groups_2')

                # If both specific_category and pnns_groups_2 are null, return an error
                if not specific_category:
                    return JsonResponse({'error': 'No category found for the product'}, status=404)
<<<<<<< Updated upstream
                
                # Retrieve products with the same category but not from the same collection
                products_with_same_category = dbname.food.find({'pnns_groups_1': specific_category})
                for product in products_with_same_category:
                    print(product)
=======

                # Retrieve products with the same category but not from the same collection
                products_with_same_category = dbname.food.find({'pnns_groups_1': specific_category})
>>>>>>> Stashed changes

                if collection_name == "food":
                    # Filter products based on score
                    products_with_same_category = [product for product in products_with_same_category if product.get('nutriscore_score_out_of_100', 0) >= current_product_score]
                    # Sort the products by nutriscore_score_out_of_100
                    sorted_products = sorted(products_with_same_category, key=lambda x: x.get('nutriscore_score_out_of_100', 0), reverse=True)
                else:
<<<<<<< Updated upstream
                    if collection_name == "cosmetics":
                        # Filter products based on score
                        products_with_same_category = [product for product in products_with_same_category]

                        # Sort the products by _id
                        sorted_products = sorted(products_with_same_category, key=lambda x: x['_id'], reverse=True)

                print(products_with_same_category)
=======
                    # Filter products based on score
                    products_with_same_category = [product for product in products_with_same_category if product.get('score', 0) >= current_product_score]
                    sorted_products = sorted(products_with_same_category, key=lambda x: x.get('score', 0), reverse=True)
>>>>>>> Stashed changes

                # Serialize the products
                serialized_products = []
                if len(sorted_products) >= 5:
                    # If the list contains at least 5 elements, loop through the first 5 elements
                    for p in sorted_products[:5]:
                        # Convert ObjectId to string for serialization
                        p['_id'] = str(p['_id'])
                        # Convert p to JSON
                        serialized_product = json.dumps(p, default=str)
                        serialized_products.append(serialized_product)
                else:
                    # If the list contains fewer than 5 elements, loop through all the elements
                    for p in sorted_products:
                        # Convert ObjectId to string for serialization
                        p['_id'] = str(p['_id'])
                        # Convert p to JSON
                        serialized_product = json.dumps(p, default=str)
                        serialized_products.append(serialized_product)

                # Return the serialized products
                return JsonResponse({'Alternatives': serialized_products})

            else:
                return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
