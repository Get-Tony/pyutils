# Random Python Scripts

This repository is a collection of random Python scripts created with the intention of possibly aiding someone, someday. The scripts are compatible with Python version 3.10.0 or higher.

I hope that these will be of help to you or spark some ideas for your own projects!

## Formatting and Linting

Formatting and linting are enforced using the checks below on Push events with GitHub Actions. Please run the checks locally before pushing any changes.

```bash
black $(git ls-files '*.py') --check --line-length 79
pylint $(git ls-files '*.py')
```

## License

All scripts within this repository are licensed under the [MIT License](LICENSE).

## Contributions

Improvement suggestions are very welcome! Feel free to open an issue or submit a pull request if you have any enhancements or fixes.

## Issues

For any questions or discussions, please [Create an Issue](https://github.com/Get-Tony/pyutils/issues).
