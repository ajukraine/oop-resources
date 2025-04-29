print("Pattern Adapter")


class WebAccountProvider:
  def authorize(self, user):
    is_authenticated = user.authenticate()
    if is_authenticated:
      print("User is authorized")


class GoogleAccount:
  def login(self):
    print("Account is logged on")


class GithubAccount:
  def enter(self):
    print("Account entered the Github")


class UserAdapterForGoogle:
  def __init__(self, google_account):
    self.google_account = google_account

  def authenticate(self):
    self.google_account.login()


class UserAdapterForGithub:
  def __init__(self, github_account):
    self.github_account = github_account

  def authenticate(self):
    self.github_account.enter()


google = GoogleAccount()
google.login()

github = GithubAccount()
github.enter()

provider = WebAccountProvider()
provider.authorize(UserAdapterForGoogle(google))
provider.authorize(UserAdapterForGithub(github))
