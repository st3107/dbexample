from rever.activity import activity


@activity
def build_docs():
    make -C docs html


@activity
def install():
    python -m pip install .


$PROJECT = 'dbexample'
$ACTIVITIES = [
    'version_bump',
    'changelog',
    'build_docs',
    'tag',
    'install',
    'push_tag',
    'ghrelease',
    'gh-pages'
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

$SPHINX_HOST_DIR = 'docs/build'
$GHPAGES_REPO = 'git@github.com:st3107/dbexample.git'
$GHPAGES_BRANCH = 'gh-pages'
$GHPAGES_COPY = (
    ('$SPHINX_HOST_DIR/html', '$GHPAGES_REPO_DIR'),
)
