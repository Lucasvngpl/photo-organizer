#!/usr/bin/env python3
"""
Demo script showing how to use the Photo Organizer.
This demonstrates the API without requiring actual images or TensorFlow installation.
"""

from pathlib import Path


def demo_basic_usage():
    """Demonstrate basic usage of the photo organizer."""
    print("="*60)
    print("PHOTO ORGANIZER - USAGE DEMO")
    print("="*60)
    print()
    
    print("1. BASIC USAGE")
    print("-" * 40)
    print("Command:")
    print("  python organizer.py /path/to/photos")
    print()
    print("What it does:")
    print("  • Scans all images in the directory")
    print("  • Uses EfficientNet to classify each image")
    print("  • Moves homework-related images to 'school_photos/' folder")
    print("  • Keeps regular photos in original location")
    print()
    
    print("2. DRY RUN (TEST MODE)")
    print("-" * 40)
    print("Command:")
    print("  python organizer.py /path/to/photos --dry-run")
    print()
    print("What it does:")
    print("  • Shows what WOULD happen without moving files")
    print("  • Perfect for testing before actual organization")
    print()
    
    print("3. CUSTOM OUTPUT FOLDER")
    print("-" * 40)
    print("Command:")
    print("  python organizer.py /path/to/photos --homework-dir study_materials")
    print()
    print("What it does:")
    print("  • Moves homework images to custom folder instead of 'school_photos/'")
    print()
    
    print("4. SINGLE IMAGE CLASSIFICATION")
    print("-" * 40)
    print("Command:")
    print("  python classifier.py photo.jpg")
    print()
    print("What it does:")
    print("  • Classifies a single image")
    print("  • Shows if it's homework-related")
    print("  • Displays confidence score and prediction")
    print()
    
    print("="*60)
    print("EXAMPLE WORKFLOW")
    print("="*60)
    print()
    print("Step 1: Setup")
    print("  $ pip install -r requirements.txt")
    print()
    print("Step 2: Test with dry run")
    print("  $ python organizer.py ~/Pictures/camera --dry-run")
    print()
    print("Step 3: Review the results")
    print("  [Output shows what would be moved]")
    print()
    print("Step 4: Run for real")
    print("  $ python organizer.py ~/Pictures/camera")
    print()
    print("Step 5: Check results")
    print("  $ ls school_photos/")
    print("  [Shows moved homework images]")
    print()


def demo_code_usage():
    """Demonstrate using the organizer as a Python library."""
    print("="*60)
    print("USING AS PYTHON LIBRARY")
    print("="*60)
    print()
    
    code_example = '''
# Example 1: Basic usage
from organizer import PhotoOrganizer

organizer = PhotoOrganizer(source_dir="/path/to/photos")
stats = organizer.organize_photos()

print(f"Organized {stats['homework']} homework photos")

# Example 2: With custom settings
organizer = PhotoOrganizer(
    source_dir="/path/to/photos",
    homework_dir="my_study_folder"
)
stats = organizer.organize_photos(dry_run=True)

# Example 3: Just classification
from classifier import HomeworkImageClassifier

classifier = HomeworkImageClassifier()
is_homework, confidence, prediction = classifier.is_homework_related("image.jpg")

if is_homework:
    print(f"This is homework! ({prediction}, {confidence:.2%} confidence)")
else:
    print(f"Regular photo ({prediction})")

# Example 4: Batch classification
image_paths = ["img1.jpg", "img2.jpg", "img3.jpg"]
results = classifier.classify_batch(image_paths)

for path, is_hw, conf, pred in results:
    print(f"{path}: {'HOMEWORK' if is_hw else 'REGULAR'} ({pred})")
'''
    
    print("Python Code Examples:")
    print(code_example)


def demo_classification_examples():
    """Show examples of what gets classified as homework."""
    print("="*60)
    print("CLASSIFICATION EXAMPLES")
    print("="*60)
    print()
    
    print("HOMEWORK-RELATED (will be moved):")
    print("  ✓ Photos of textbook pages")
    print("  ✓ Whiteboard pictures from class")
    print("  ✓ Blackboard notes")
    print("  ✓ Screenshots of educational websites")
    print("  ✓ Pictures of notebooks and notes")
    print("  ✓ Calculator displays")
    print("  ✓ Computer screen with study materials")
    print("  ✓ Desk with study materials")
    print()
    
    print("REGULAR PHOTOS (will be kept):")
    print("  ○ Vacation photos")
    print("  ○ Selfies and portraits")
    print("  ○ Food pictures")
    print("  ○ Nature and landscapes")
    print("  ○ Social gathering photos")
    print("  ○ Pet pictures")
    print()


def demo_android_info():
    """Show Android-specific information."""
    print("="*60)
    print("ANDROID ADAPTATION")
    print("="*60)
    print()
    
    print("This Python template can be adapted for Android!")
    print()
    print("See ANDROID_GUIDE.md for:")
    print("  • Converting model to TensorFlow Lite")
    print("  • Android project structure (Kotlin)")
    print("  • MediaStore integration")
    print("  • Background processing with WorkManager")
    print("  • Creating hidden albums")
    print("  • Complete code examples")
    print()
    print("Quick Start for Android:")
    print("  1. Convert EfficientNet to TFLite format")
    print("  2. Create Android Studio project")
    print("  3. Add TFLite dependencies")
    print("  4. Implement classifier in Kotlin")
    print("  5. Use MediaStore API to organize photos")
    print()


def main():
    """Run all demos."""
    demo_basic_usage()
    print("\n\n")
    demo_code_usage()
    print("\n\n")
    demo_classification_examples()
    print("\n\n")
    demo_android_info()
    print("\n\n")
    
    print("="*60)
    print("For more information, see README.md")
    print("="*60)


if __name__ == "__main__":
    main()
