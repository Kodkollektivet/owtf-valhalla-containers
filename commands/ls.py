class Ls:
    def info():
        """Returns info about the command"""
        return {"info": "Ls is a tool for listing folder content"}

    def run(params):
        """Run the actual command output"""
        return {
            "commmand": "ls",
            "result": "the actual result",
            "params": params
        }

