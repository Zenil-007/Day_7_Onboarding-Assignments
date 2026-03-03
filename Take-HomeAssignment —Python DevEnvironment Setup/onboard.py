"""
Developer Onboarding Environment Check Script
Performs multiple checks to validate Python development setup.
"""

import sys
import time
import shutil
import argparse
import subprocess
from typing import Dict, Tuple
import importlib
import pkg_resources

MIN_PYTHON = (3, 10)
DISK_WARNING_THRESHOLD = 1 * 1024 * 1024 * 1024  # 1 GB


def check_python_version() -> Tuple[bool, str]:
    """Check if Python version is >= 3.10."""
    version = sys.version_info
    if version >= MIN_PYTHON:
        return True, f"{version.major}.{version.minor}.{version.micro}"
    return False, f"{version.major}.{version.minor}.{version.micro}"


def check_virtual_env() -> Tuple[bool, str]:
    """Check if script is running inside a virtual environment."""
    if sys.prefix != sys.base_prefix:
        return True, sys.prefix
    return False, "Not in virtual environment"


def list_installed_packages() -> Dict[str, str]:
    """Return installed packages and versions."""
    packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return packages


def check_package_installed(package_name: str) -> Tuple[bool, str]:
    """Check if a package is installed."""
    spec = importlib.util.find_spec(package_name)
    if spec is not None:
        version = pkg_resources.get_distribution(package_name).version
        return True, version
    return False, "Not Installed"


def check_internet_connectivity() -> Tuple[bool, str]:
    """Check internet connectivity using requests."""
    try:
        import requests  # pylint: disable=import-outside-toplevel

        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            return True, "Internet reachable"
        return False, "Response received but not OK"
    except Exception as exc:  # pylint: disable=broad-except
        return False, str(exc)


def check_disk_space() -> Tuple[bool, str]:
    """Check available disk space."""
    total, used, free = shutil.disk_usage("/")
    if free < DISK_WARNING_THRESHOLD:
        return False, f"Low disk space: {free / (1024**3):.2f} GB free"
    return True, f"{free / (1024**3):.2f} GB free"


def attempt_fix(package_name: str) -> None:
    """Attempt to install a missing package."""
    subprocess.run(
        [sys.executable, "-m", "pip", "install", package_name],
        check=False,
    )


def timed_check(func):
    """Decorator to measure execution time of checks."""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        return result, duration

    return wrapper


@timed_check
def run_check(func, *args):
    """Execute a check function."""
    return func(*args)


def generate_report(results: Dict[str, Tuple[bool, str, float]]) -> str:
    """Generate formatted report."""
    report_lines = ["=== Developer Onboarding Check ==="]
    passed = 0

    for check_name, (status, message, duration) in results.items():
        label = "PASS" if status else "FAIL"
        report_lines.append(
            f"[{label}] {check_name}: {message} " f"(Time: {duration:.4f}s)"
        )
        if status:
            passed += 1

    total = len(results)
    report_lines.append("---")
    report_lines.append(f"Result: {passed}/{total} checks passed")
    return "\n".join(report_lines)


def save_report(report: str) -> None:
    """Save report to setup_report.txt."""
    with open("setup_report.txt", "w", encoding="utf-8") as file:
        file.write(report)


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Developer Onboarding Environment Check"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show installed packages",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to fix missing packages",
    )
    args = parser.parse_args()

    results = {}

    # Python version
    (status, message), duration = run_check(check_python_version)
    results["Python Version"] = (status, message, duration)

    # Virtual environment
    (status, message), duration = run_check(check_virtual_env)
    results["Virtual Environment"] = (status, message, duration)

    # pylint
    (status, message), duration = run_check(check_package_installed, "pylint")
    if not status and args.fix:
        attempt_fix("pylint")
    results["pylint Installed"] = (status, message, duration)

    # black
    (status, message), duration = run_check(check_package_installed, "black")
    if not status and args.fix:
        attempt_fix("black")
    results["black Installed"] = (status, message, duration)

    # numpy
    (status, message), duration = run_check(check_package_installed, "numpy")
    results["numpy Installed"] = (status, message, duration)

    # Internet
    (status, message), duration = run_check(check_internet_connectivity)
    results["Internet Connectivity"] = (status, message, duration)

    # Disk space
    (status, message), duration = run_check(check_disk_space)
    results["Disk Space"] = (status, message, duration)

    report = generate_report(results)
    print(report)
    save_report(report)

    if args.verbose:
        print("\nInstalled Packages:")
        packages = list_installed_packages()
        for name, version in sorted(packages.items()):
            print(f"{name}=={version}")


if __name__ == "__main__":
    main()
