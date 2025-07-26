from collections import deque

class BrowserHistory:
    def __init__(self, max_size=5):
        self.history = deque(maxlen=max_size)       
        self.forward_stack = deque()                

    def add_page(self, url):
        self.history.append(url)
        self.forward_stack.clear() 
        self._print_state(f"Added page: {url}")

    def go_back(self):
        if len(self.history) > 1:
            last_page = self.history.pop()
            self.forward_stack.append(last_page)
            self._print_state(f"Went back from: {last_page}")
        else:
            print("Cannot go back: Not enough history.")

    def go_forward(self):
        if self.forward_stack:
            next_page = self.forward_stack.pop()
            self.history.append(next_page)
            self._print_state(f"Went forward to: {next_page}")
        else:
            print("Cannot go forward: Forward stack is empty.")

    def _print_state(self, action):
        print(f"\n{action}")
        print(f"Current History: {list(self.history)}")
        print(f"Forward Stack: {list(self.forward_stack)}")



browser = BrowserHistory()


browser.add_page("google.com")
browser.add_page("openai.com")
browser.add_page("github.com")
browser.add_page("stackoverflow.com")
browser.add_page("reddit.com")


browser.add_page("masaischool.com")  

browser.go_back()
browser.go_back()

browser.go_forward()
browser.add_page("python.org") 

browser.go_back()
