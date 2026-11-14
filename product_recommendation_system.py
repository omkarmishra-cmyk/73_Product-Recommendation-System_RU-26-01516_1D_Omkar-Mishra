
# Product Recommendation System

purchases = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"]
}


# Function to calculate Jaccard similarity
def jaccard_similarity(products1, products2):
    set1 = set(products1)
    set2 = set(products2)

    common = len(set1 & set2)
    total = len(set1 | set2)

    if total == 0:
        return 0.0

    return common / total


# Function to find the most popular product
def popular_product(purchases):
    counts = {}

    for products in purchases.values():
        for product in products:
            counts[product] = counts.get(product, 0) + 1

    # Highest count first; insertion order breaks ties
    product = max(counts, key=counts.get)
    return product, counts[product]


# Main recommendation function
def recommend_customer(name):
    name = name.strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name not in purchases:
        print(f"Customer '{name}' not found.")
        return

    scores = {}

    # Compare the selected customer with everyone else
    for customer in purchases:
        if customer != name:
            scores[customer] = jaccard_similarity(
                purchases[name],
                purchases[customer]
            )

    # Sort from highest similarity to lowest
    scores = dict(
        sorted(scores.items(), key=lambda item: item[1], reverse=True)
    )

    # Check whether any customer has positive similarity
    if max(scores.values(), default=0) == 0:
        print("No similar customers found.")

        product, count = popular_product(purchases)
        print(f"Popular product: {product} (bought by {count} customers)")
        return

    print(f"Similarity scores:")

    for customer, score in scores.items():
        print(f"{customer} : {score:.2f}")

    # Get the customer with the highest similarity
    most_similar = max(scores, key=scores.get)

    print(f"Most similar customer: {most_similar}")

    # Find products owned by the similar customer but not by us
    selected_products = set(purchases[name])
    similar_products = set(purchases[most_similar])

    new_products = similar_products - selected_products

    if new_products:
        # Keep the original purchase-list order for the recommendation
        for product in purchases[most_similar]:
            if product not in selected_products:
                print(f"Recommended: {product}")
                break
    else:
        print("No new products to recommend.")


# Program starts here
name = input("Recommend for: ")
recommend_customer(name)
