# Homework 1 — Finding Textually Similar Documents

## 📘 Description
This notebook explores methods for detecting **textual similarity** between documents using three core techniques in data mining:
- **Shingling** for document representation
- **MinHashing** for efficient similarity approximation
- **Locality-Sensitive Hashing (LSH)** for scalable candidate pair detection

The dataset used consists of multiple *lasagna recipe* texts, offering a controlled yet diverse set of documents for testing textual similarity algorithms.

## 🧩 Contents
The notebook is structured as follows:
- Homework 1 — Finding Textually Similar Documents
- Context and Objective
- 1. Loading and Inspecting the Dataset
- 2. Shingling: Representing Documents as Sets
- 3. Computing Exact Jaccard Similarity
- Visualizing Jaccard Similarities
- 4. MinHashing: Efficient Similarity Estimation
- Comparing Exact and Estimated Similarities
- 5. Locality-Sensitive Hashing (LSH)
- Evaluating LSH Parameters
- 6. Conclusion

## 🧰 Requirements
You can install all required packages using `pip install -r requirements.txt`.

## ⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/StRomano02/Data-Mining-Project.git
   cd Data-Mining-Project/homework1
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the notebook**
   ```bash
   jupyter notebook homework1_analysis.ipynb
   ```

## 👥 Authors
- **Stefano Romano**
- **Marco Cecilia**
