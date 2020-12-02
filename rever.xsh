$PROJECT = 'dbexample'
$ACTIVITIES = [
    'version_bump',
    'changelog',
    'tag',
    'push_tag',
    'pypi'
]

$VERSION_BUMP_PATTERNS = [
    ('dbexample/__init__.py', r'__version__\s*=.*', "__version__ = '$VERSION'"),
    ('setup.py', r'version\s*=.*,', "version='$VERSION',")
]

$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_TEMPLATE = 'TEMPLATE.rst'
$TAG_REMOTE = 'git@github.com:st3107/dbexample.git'

$GITHUB_ORG = 'st3107'
$GITHUB_REPO = 'dbexample'
