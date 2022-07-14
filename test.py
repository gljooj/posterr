from src.controller.profile_controller import Profile


def test():
    Profile(username="gabtest", page=2).profile_page()
    print('ok')
