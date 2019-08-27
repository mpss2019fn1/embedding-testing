import argparse
import csv
import logging
from pathlib import Path
from typing import List, Dict, Tuple

import Levenshtein

from src.Testing.FileParsing.EntityLabelFileParsing.entity_label_file_parser import EntityLabelFileParser


def main(args):
    logging.basicConfig(format="%(asctime)s : [%(process)s] %(levelname)s : %(message)s", level=logging.INFO)
    logging.info(f"loading entity labels...")
    entity_labels = EntityLabelFileParser.create_from_file(args.labels)
    linking_candidates: Dict[str, List[str]] = _load_links(args.links)

    with args.output.open("w+") as output_stream:
        csv_writer: csv.writer = csv.writer(output_stream)
        csv_writer.writerow(["embedding_label", "knowledgebase_id"])
        for knowledgebase_id in linking_candidates:
            tags: List[str] = linking_candidates[knowledgebase_id]
            if len(tags) < 2:
                csv_writer.writerow([tags[0], knowledgebase_id])
                continue
            csv_writer.writerow([_disambiguate_links(tags, entity_labels[knowledgebase_id]), knowledgebase_id])


def _load_links(link_file: Path) -> Dict[str, List[str]]:
    logging.info(f"loading entity linkings...")
    linking_candidates: Dict[str, List[str]] = {}
    with link_file.open("r") as csv_stream:
        csv_reader: csv.reader = csv.reader(csv_stream)
        next(csv_reader)
        for line in csv_reader:
            if not line:
                continue

            knowledge_base_id: str = line[1]
            embedding_tag: str = line[0]

            if knowledge_base_id not in linking_candidates:
                linking_candidates[knowledge_base_id] = []

            linking_candidates[knowledge_base_id].append(embedding_tag)

    return linking_candidates


def _disambiguate_links(tags: List[str], label: str) -> str:
    if label.upper() in tags:
        return label.upper()

    if label.lower() in tags:
        return label.lower()

    if label.capitalize() in tags:
        return label.capitalize()

    similarities: List[Tuple[str, float]] = []
    for tag in tags:
        similarities.append((tag, Levenshtein.ratio(tag, label)))

    similarities.sort(key=lambda x: x[1], reverse=True)

    if similarities[0][1] < 0.5:
        print(f"[WARNING]: No good match for {label}: {similarities}")
    return similarities[0][0]


def _initialize_parser():
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        "--links",
        type=Path,
        help="Path to the file containing linkings.",
        required=True
    )
    argument_parser.add_argument(
        "--labels",
        type=Path,
        help=f"Path to the file containing labels",
        required=True
    )
    argument_parser.add_argument(
        "--output",
        type=Path,
        help=f"Path to the desire output file",
        required=True
    )

    return argument_parser


if __name__ == "__main__":
    parser = _initialize_parser()
    main(parser.parse_args())
