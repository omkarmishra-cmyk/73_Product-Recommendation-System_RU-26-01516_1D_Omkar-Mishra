# Product Recommendation System

## 1. Project Overview

The Product Recommendation System is a Python-based project that recommends products to customers based on their purchasing history.

It uses **Jaccard Similarity** to identify the customer whose purchased products are most similar to the selected customer. It then recommends a product that the selected customer has not purchased yet.

If no similar customer is found, the system recommends the most popular product based on purchase frequency.

## 2. Objectives

- To understand customer purchasing patterns.
- To calculate similarity between customers using Jaccard Similarity.
- To identify the most similar customer.
- To recommend products that the selected customer has not purchased.
- To find the most popular product when no similar customers exist.
- To implement Python concepts such as dictionaries, lists, sets, loops, and functions.

## 3. Technologies Used

- Programming Language: Python 3
- Editor: VS Code / IDLE
- Concepts: Dictionaries, Lists, Sets, Functions, Loops, Conditional Statements, Sorting.

## 4. Dataset

The project uses the following sample customer purchase data:

| Customer | Purchased Products                |
| -------- | --------------------------------- |
| Amit     | Laptop, Mouse, Keyboard           |
| Bina     | Laptop, Mouse, Headphones         |
| Chetan   | Phone, Charger                    |
| Divya    | Laptop, Keyboard, Monitor, Webcam |

## 5. Algorithm

1. Store customer names and their purchased products in a dictionary.
2. Take the customer name as input.
3. Validate the customer name.
4. Convert purchase lists into sets.
5. Calculate Jaccard Similarity between the selected customer and all other customers.
6. Sort similarity scores in descending order.
7. Identify the most similar customer.
8. Recommend a product that the selected customer has not purchased.
9. If all similarity scores are zero, display the most popular product.

## 6. Jaccard Similarity Formula

Jaccard Similarity = Number of Common Products / Number of Distinct Products

J(A, B) = |A ∩ B| / |A ∪ B|

## 7. Features

- Customer input validation.
- Similarity calculation using Jaccard Similarity.
- Similarity scores displayed up to two decimal places.
- Automatic identification of the most similar customer.
- Product recommendation based on purchase history.
- Popular product recommendation when no similar customer exists.

## 8. How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python product_recommendation.py
```

5. Enter a customer name when prompted.

## 9. Test Cases

| Test Case | Input       | Expected Result         |
| --------- | ----------- | ----------------------- |
| 1         | Amit        | Recommend Headphones    |
| 2         | Chetan      | Popular product: Laptop |
| 3(a)      | Zara        | Customer not found      |
| 3(b)      | Empty input | Name cannot be empty    |
| 4         | Bina        | Recommend Keyboard      |

## 10. Conclusion

This project demonstrates a basic product recommendation technique using Jaccard Similarity. It helps identify similar customers and recommend products based on their purchasing patterns. It also demonstrates the practical application of Python programming concepts.

## 11. Future Scope

- Use a larger customer purchase dataset.
- Recommend multiple products.
- Integrate the system with an online shopping website.
- Use machine learning techniques for advanced recommendations.

## Author

**Omkar Mishra**

**Language:** Python 3
