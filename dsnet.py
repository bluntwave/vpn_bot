import subprocess
class Dsnet:
    def __init__(self, username, description):
        self.username = username
        self.owner = 'test'
        self.description = description

    def create_user(self):
        out = None
        subprocess.run(['dsnet', 'add', self.username, '--owner', self.owner, '--description', self.description, '--confirm'], stdout=out)
        print(out)
        return out