import itertools
from pathlib import Path
from zipfile import ZipFile

grid_size = 8

package_dir = Path("packages")

wheel_file_contents = """
Wheel-Version: 1.0
Generator: nqueens (1.0.0)
Root-Is-Purelib: true
Tag: py3-none-any
""".strip()


def to_name(column: int) -> str:
    return f"queen_{chr(ord('a') + column)}"


def to_version(row: int) -> str:
    return f"{row + 1}"


def exclude(column: int, row: int) -> str:
    return f"{to_name(column)} != {to_version(row)}"


def generate_package(column: int, row: int) -> None:
    name = to_name(column)
    version = to_version(row)
    dependencies = [
        exclude(c, r)
        for c, r in itertools.product(range(grid_size), repeat=2)
        if (
            # column exclusion (row exclusion is implicit)
            (r == row and c != column)
            # diagonal exclusion
            or ((d_c := abs(c - column)) == (d_r := abs(r - row)) and (d_c or d_r))
        )
    ]

    # Write the wheel
    filename = f"{name}-{version}-py3-none-any.whl"
    with ZipFile(package_dir.joinpath(filename), "w") as writer:
        metadata = [f"Name: {name}", f"Version: {version}", "Metadata-Version: 2.2"]
        for requires_dist in dependencies:
            metadata.append(f"Requires-Dist: {requires_dist}")
        writer.writestr(f"{name}-{version}.dist-info/METADATA", "\n".join(metadata))
        writer.writestr(f"{name}-{version}.dist-info/WHEEL", wheel_file_contents)
        # Not checked anyway
        record = f"{name}-{version}.dist-info/METADATA,,"
        record += f"{name}-{version}.dist-info/WHEEL,,"
        record += f"{name}-{version}.dist-info/RECORD,,"
        writer.writestr(f"{name}-{version}.dist-info/RECORD", "")


def main():
    package_dir.mkdir(exist_ok=True, parents=True)
    for column in range(grid_size):
        for row in range(grid_size):
            generate_package(column, row)


if __name__ == "__main__":
    main()
