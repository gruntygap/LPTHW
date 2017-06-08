from flask import Flask
from flask_classful import FlaskView

# we'll make a list to hold some quotes for our app
quotes = [
    "A noble spirit embiggens the smallest man! ~ Jebediah Springfield",
    "If there is a way to do it better... find it. ~ Thomas Edison",
    "No one knows what he can do till he tries. ~ Publilius Syrus"
]

app = Flask(__name__)


class QuotesTwoView(FlaskView):
    def index(self):
        return "<br>".join(quotes)

    def test(self):
        return "test"
QuotesTwoView.register(app)

if __name__ == '__main__':
    app.run()

# http://localhost:5000/quotestwo/
