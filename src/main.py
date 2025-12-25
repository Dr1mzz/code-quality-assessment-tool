"""
Точка входа для Инструмента оценки качества кода.

Этот скрипт предоставляет интерфейс командной строки для анализа качества Python кода.
"""

import argparse
import sys
from pathlib import Path

from src.analyzer import CodeAnalyzer
from src.reporter import ReportGenerator


def main():
    """Main function to run the code quality analyzer."""
    parser = argparse.ArgumentParser(
        description="Инструмент оценки качества кода - Анализ качества Python кода"
    )
    parser.add_argument(
        "target",
        type=str,
        help="Файл или директория для анализа"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Путь к файлу для сохранения отчета"
    )
    parser.add_argument(
        "--format",
        "-f",
        type=str,
        choices=["text", "json"],
        default="text",
        help="Формат вывода (text или json)"
    )
    parser.add_argument(
        "--report-dir",
        type=str,
        default="reports",
        help="Директория для сохранения отчетов (по умолчанию: reports)"
    )

    args = parser.parse_args()

    # Check if target exists
    target_path = Path(args.target)
    if not target_path.exists():
        print(f"Ошибка: {args.target} не существует", file=sys.stderr)
        return 1

    # Initialize analyzer and reporter
    analyzer = CodeAnalyzer()
    reporter = ReportGenerator(output_dir=args.report_dir)

    # Analyze
    if target_path.is_file():
        if not target_path.suffix == ".py":
            print("Ошибка: Целевой файл должен быть Python файлом (.py)", file=sys.stderr)
            return 1
        print(f"Анализ файла: {args.target}")
        analysis = analyzer.analyze_file(str(target_path))
    else:
        print(f"Анализ директории: {args.target}")
        analysis = analyzer.analyze_directory(str(target_path))

    # Generate report
    if "error" in analysis:
        print(f"Ошибка при анализе: {analysis['error']}", file=sys.stderr)
        return 1

    if args.format == "json":
        report = reporter.generate_json_report(analysis, output_file=args.output)
    else:
        report = reporter.generate_text_report(analysis, output_file=args.output)

    # Print report to stdout if no output file specified
    if args.output is None:
        print(report)

    print("\nАнализ завершен!", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

