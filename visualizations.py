from collections import Counter
import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, data):
        self.labels = data
        self.counts = Counter(self.labels)

    def plot_histogram(self):
        plt.bar(self.counts.keys(), self.counts.values(), color='tomato')
        plt.xlabel('Emotion')
        plt.ylabel('# of songs')
        plt.title('Emotion Distribution in my favourite songs')
        plt.show()