import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Data format converter')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        print(f"Converting from {args.input_file} to {args.output_file}")
        # Tutaj będzie dalsza logika konwersji
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
