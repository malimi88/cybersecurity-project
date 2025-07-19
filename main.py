"""
Penetration Testing Toolkit Main Entry Point
"""

import argparse
from modules import scanner, exploiter, reporter

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument('--scan', help="Target to scan")
    parser.add_argument('--exploit', help="Exploit target")
    parser.add_argument('--report', help="Generate report")
    args = parser.parse_args()

    if args.scan:
        scanner.run_scan(args.scan)
    if args.exploit:
        exploiter.run_exploit(args.exploit)
    if args.report:
        reporter.generate_report(args.report)

if __name__ == '__main__':
    main()
