Social Media Content Sanitizer (Python Mini Project)
Project Overview

The Social Media Content Sanitizer is a Python-based mini project developed to simulate a moderation system for a school-safe social media platform. The system automatically scans user posts, detects inappropriate language, replaces banned words with masked symbols (***) and extracts suspicious web links for security verification.

This project demonstrates how basic Python programming concepts can be applied to build a real-world content filtering tool.

Objective

The objective of this project is to:

Detect banned or unsafe words in social media posts
Replace inappropriate words with masked symbols (***)
Extract web links from posts
Store extracted links for security checking
Track violations made by users
Generate a moderation summary report
Save cleaned posts into a safe output file
Technologies Used
Programming Language: Python
Concepts Applied:
Lists
Dictionaries
Functions
Regular Expressions (Regex)
File Handling
Loops and Conditions
Project Structure
SocialMediaContentSanitizer/
│
├── sanitizer.py
├── posts.txt
├── cleaned_posts.txt
├── links_found.txt
└── README.md

Input File Description

The program reads posts from:

posts.txt

Example content:

User123: This is a bad post check http://example.com
User456: I love learning Python
User123: Stop spreading hate visit https://dangerous-link.com
User789: This platform is toxic sometimes
Output Files Generated

1. Cleaned Posts File
cleaned_posts.txt

Contains sanitized posts where banned words are replaced.

Example:

User123: This is a *** post check http://example.com
User123: Stop spreading *** visit https://dangerous-link.com

2. Extracted Links File
links_found.txt

Contains all detected URLs from posts.

Example:

http://example.com
https://dangerous-link.com
Features
Automatic detection of banned words
Case-insensitive word filtering
Replacement of unsafe words with ***
URL extraction using Regex
User violation tracking system
Automatic input file generation if missing
Summary moderation report generation
Output saved into separate files