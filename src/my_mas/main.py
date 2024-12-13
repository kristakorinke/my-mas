#!/usr/bin/env python
import sys
import warnings
import os
import random

from my_mas.crew import MyMas

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def ensure_blog_posts_directory():
    """Ensure the blog_posts directory exists."""
    os.makedirs('blog_posts', exist_ok=True)

def run(topic=None):
    """
    Run the crew to generate a blog post.
    Optionally specify a topic, otherwise generate a random security topic.
    """
    ensure_blog_posts_directory()
    
    inputs = {
        'topic': topic or generate_security_topic()
    }
    MyMas().crew().kickoff(inputs=inputs)

def generate_security_topic():
    """
    Generate a random unique security topic.
    """
    security_topics = [
        'IoT Device Security',
        'Home Network Protection',
        'Smart Lock Technologies',
        'Preventing Cyber Attacks',
        'Privacy in Smart Homes',
        'Business Security Strategies',
        'Emerging Home Security Tech',
        'Protecting Against Social Engineering',
        'Secure Smart Home Setup',
        'Cybersecurity for Small Businesses',
        'Wireless Network Security',
        'Physical Security Integration',
        'Remote Monitoring Technologies',
        'Smart Camera Systems',
        'Biometric Access Control'
    ]
    
    return random.choice(security_topics)

def main():
    """Main entry point with command-line argument support."""
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run()

if __name__ == "__main__":
    main()