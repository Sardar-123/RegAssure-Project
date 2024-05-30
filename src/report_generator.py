from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import numpy as np

def generate_report(similarity_info, report_path, similarity_percentage):
    c = canvas.Canvas(report_path, pagesize=letter)
    c.drawString(100, 750, "XSD Comparison Report")

    y = 700
    for info in similarity_info:
        c.drawString(100, y, f"Element1: {info['element1']} - Element2: {info['element2']} Similarity: {info['similarity']:.2f}")
        y -= 30

    # Add similarity percentage
    c.drawString(100, y - 30, f"Overall Similarity: {similarity_percentage:.2f}%")

    # Save the PDF
    c.save()

def generate_similarity_graph(similarity_info, graph_path):
    similarities = [info['similarity'] for info in similarity_info]
    plt.hist(similarities, bins=10, range=(0, 1), alpha=0.75, color='blue')
    plt.title('Similarity Distribution Between XSD Elements')
    plt.xlabel('Similarity Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(graph_path)
    plt.close()