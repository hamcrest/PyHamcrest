# Contributing to PyHamcrest

Thank you for your interest in contributing to PyHamcrest! This guide will help you get started.

## Table of Contents

- [Development Setup](#development-setup)
- [Running Tests](#running-tests)
- [Code Style and Linting](#code-style-and-linting)
- [Type Checking](#type-checking)
- [Adding Changelog Entries](#adding-changelog-entries)
- [Submitting Pull Requests](#submitting-pull-requests)
- [Release Process](#release-process-for-maintainers)

## Development Setup

### Prerequisites

- Python 3.10 or later (Python 3.14 recommended for development)
- Git

### Installation

1. Fork and clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/PyHamcrest.git
cd PyHamcrest
```

2. Install development dependencies:

We recommend using [uv](https://github.com/astral-sh/uv) for fast dependency resolution:

```bash
pip install uv
uv pip install -e ".[dev]"
```

Or using pip directly:

```bash
pip install -e ".[dev]"
```

3. Install pre-commit hooks:

```bash
pre-commit install
```

This ensures code style checks run automatically before each commit.

## Running Tests

### Quick Test Run

Run tests with pytest:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/hamcrest_unit_test/core/isequal_test.py
```

Run a specific test:

```bash
pytest tests/hamcrest_unit_test/core/isequal_test.py::TestClass::test_name
```

### Test Coverage

Run tests with coverage:

```bash
coverage run -m pytest
coverage report
```

### Testing Across Python Versions

We use [tox](https://tox.wiki/) to test across multiple Python versions:

```bash
# Test all available Python versions (skips missing interpreters)
tox -s

# Test specific Python version
tox -e py312

# Test with numpy support
tox -e py312-numpy
```

**IMPORTANT**: Always run `tox -s` before submitting a pull request to verify tests pass across all available Python versions. The `-s` flag skips missing interpreters.

### Supported Python Versions

- Python 3.10, 3.11, 3.12, 3.13, 3.14
- PyPy 3.11

## Code Style and Linting

PyHamcrest uses automated code formatting and linting:

### Auto-formatting

Code is formatted with [Black](https://black.readthedocs.io/) and [Ruff](https://docs.astral.sh/ruff/).

Run pre-commit hooks on all files:

```bash
pre-commit run --all-files
```

Or via tox:

```bash
tox -e lint
```

### Style Notes

- Line length: 100 characters
- The codebase intentionally uses star imports (`from module import *`) to provide a clean public API
- Import order is managed by isort with a custom "hamcrests" profile

## Type Checking

PyHamcrest includes type annotations and is checked with [mypy](https://mypy-lang.org/).

Run type checking:

```bash
mypy src/
```

Or via tox:

```bash
tox -e typing
```

### Type Hint Tests

Type hints are tested using mypy with special test files in `tests/type-hinting/`. These files use a YAML format to test that type annotations work correctly. If you're adding or modifying type annotations, consider adding corresponding type tests.

## Adding Changelog Entries

**REQUIRED**: Every pull request that changes functionality must include a changelog entry.

**Exception**: Documentation-only changes (README, CONTRIBUTING, etc.) do not require changelog entries.

PyHamcrest uses [towncrier](https://towncrier.readthedocs.io/) to manage the changelog.

### How to Add a Changelog Entry

For every PR that changes code or functionality, create a changelog fragment file in the `changelog.d/` directory:

**Format**: `changelog.d/{issue_or_pr_number}.{category}.rst`

**Categories**:
- `feature` - New features or enhancements
- `bugfix` - Bug fixes
- `misc` - Miscellaneous changes (CI, docs, refactoring, etc.)

**Example**: If your PR is #123 and adds a new feature, create:

`changelog.d/123.feature.rst`:
```rst
Add support for matching custom objects with has_attributes matcher.
```

**Tips**:
- Keep descriptions concise and user-focused
- Write in the past tense ("Added", "Fixed", not "Add", "Fix")
- Don't include implementation details unless relevant to users
- The issue/PR number in the filename will be automatically linked in the generated changelog

## Submitting Pull Requests

### Before Submitting

1. ✅ Run tests: `tox -s`
2. ✅ Run linting: `pre-commit run --all-files`
3. ✅ Run type checking: `tox -e typing`
4. ✅ **Add changelog entry (REQUIRED for code changes)** - see [Adding Changelog Entries](#adding-changelog-entries)
5. ✅ Update documentation if needed

### CI Checks

When you create a pull request, GitHub Actions will automatically run:

- Tests on Python 3.10, 3.11, 3.12, 3.13, 3.14, and PyPy 3.11
- Tests on Linux, macOS, and Windows
- Linting checks
- Type checking
- Documentation build

The CI workflow runs on:
- All pull requests to `main` or `master`
- Pushes to `main`, `master`, or branches starting with `ci-testing-*`

### PR Guidelines

- **Branch naming**: Use descriptive names like `fix-issue-123` or `add-new-matcher`
- **Commit messages**: Write clear, descriptive commit messages
- **PR description**: Explain what changes you made and why
- **Link issues**: Reference related issues in your PR description (e.g., "Fixes #123")
- **Keep PRs focused**: One feature or fix per PR makes review easier

## Release Process (for Maintainers)

PyHamcrest uses automated releases via git tags.

### Creating a Release

1. Ensure all PRs for the release are merged to `main`

2. Run the release script:

```bash
./release.sh V2.2.0
```

This script:
- Creates a git tag (e.g., `V2.2.0`)
- Runs `towncrier build` to generate the changelog from fragments in `changelog.d/`
- Re-tags to include the changelog changes
- Prompts you to push the tag

3. Push the tag to trigger the release:

```bash
git push origin --tags "V2.2.0"
```

4. GitHub Actions automatically:
- Builds the package (wheel and sdist)
- Publishes to PyPI using trusted publishing
- Creates a GitHub release

### Versioning

- Format: `V{major}.{minor}.{patch}` (e.g., `V2.1.0`)
- Version is automatically derived from git tags using [hatch-vcs](https://github.com/ofek/hatch-vcs)
- No manual version bumping needed in code

## Questions?

If you have questions or need help:

- 💬 [Open a discussion](https://github.com/hamcrest/PyHamcrest/discussions)
- 🐛 [Report an issue](https://github.com/hamcrest/PyHamcrest/issues)

Thank you for contributing! 🎉
