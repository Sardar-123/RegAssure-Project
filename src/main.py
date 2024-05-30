import os
from xsd_parser import parse_xsd
from feature_extractor import extract_features
from similarity_model import create_model, train_model, compare_features
from report_generator import generate_report, generate_similarity_graph

def main():
    # Ensure the 'reports' directory exists
    report_dir = '../reports'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Step 1: Data Ingestion
    xsd_path1 = '../data/EPC115-06_2023_V1.0_pacs.008.001.08_Update.xsd'
    xsd_path2 = '../data/EPC115-06_2021_V1.0_pacs.008.001.02_Update.xsd'
    elements1 = parse_xsd(xsd_path1)
    elements2 = parse_xsd(xsd_path2)

    # Step 2: Feature Extraction
    features1 = extract_features(elements1)
    features2 = extract_features(elements2)

    # Step 3: Model Training and Comparison
    input_shape = (features1.shape[1],)
    model = create_model(input_shape)
    train_model(model, features1, features2)
    similarity_info, similarity_percentage = compare_features(model, elements1, elements2)

    # Step 4: Report Generation
    report_path = os.path.join(report_dir, 'xsd_comparison_report_new.pdf')
    generate_report(similarity_info, report_path, similarity_percentage)

    # Step 5: Graph Generation
    graph_path = os.path.join(report_dir, 'similarity_distribution.png')
    generate_similarity_graph(similarity_info, graph_path)

    print(f"Report generated: {report_path}")
    print(f"Graph generated: {graph_path}")

if __name__ == "__main__":
    main()