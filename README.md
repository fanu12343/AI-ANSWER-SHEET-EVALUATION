# Answer Sheet Evaluation System

This project is an **automated answer sheet evaluation system** that uses **OCR** for text extraction, **TF-IDF** for text vectorization, and **cosine similarity** for scoring student answers against reference answers.

---


 **OCR-based text extraction**  
- Uses an OCR engine (Tesseract or any other) to extract text from scanned answer sheet images.  

 **Text preprocessing**  
- Cleans and normalizes extracted text (stopword removal, stemming, etc.).  

**TF-IDF vectorization**  
- Converts textual answers into numerical vectors for similarity computation.  

 **Cosine Similarity Scoring**  
- Compares the student’s answer with the model answer to generate a similarity score.  

 **Backend API with Django**  
- Exposes REST APIs for uploading answer sheets and retrieving evaluation results.  

 **Automatic Marking**  
- Assigns marks based on similarity threshold and total marks.

---

## Tech Stack

- **Backend Framework**: Django (Python)
- **OCR Engine**: Tesseract OCR
- **Text Vectorization**: TF-IDF 
- **Similarity Metric**: Cosine Similarity
- **Database**: SQLite 




