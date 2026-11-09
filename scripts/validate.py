import compileall
import sys


def validate_project():
    print("Starting Python validation...")

    result = compileall.compile_dir(
        "src",
        quiet=1,
        force=True
    )

    if not result:
        print("Python validation FAILED")
        sys.exit(1)

    print("Python validation PASSED")


if __name__ == "__main__":
    validate_project()