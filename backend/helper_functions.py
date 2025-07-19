import cohere

co = cohere.Client('77wfLBnTrzMMXQsmGOmbtZJFyQT5qwC9PEM12ymT')

review = "The movie was an absolute masterpiece with stunning visuals and a gripping storyline."

response = co.classify(
model='large', # Using a pre-trained classification
inputs=[review],
examples=[
    cohere.ClassifyExample("I absolutely loved this movie, it was fantastic!", "Positive"),

    cohere.ClassifyExample("The plot was dull and boring, I didn't enjoy it at all.", "Negative"),

    cohere.ClassifyExample("The movie was okay, but nothing special.", "Neutral"),

    cohere.ClassifyExample("Great acting and direction, but the pacing was off.", "Positive"),

    cohere.ClassifyExample("I hated the ending, it ruined the whole experience.", "Negative"),

    cohere.ClassifyExample("It was just average, nothing memorable.", "Neutral")
]
)
# Print the classification result
print(f"Review: {review}")
print(f"Predicted Sentiment:{response.classifications[0].prediction}")