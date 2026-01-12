# Quick Start Guide 🚀

Get up and running with Photo Organizer in 5 minutes!

## For Complete Beginners

### Step 1: Install Python

If you don't have Python installed:

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or newer
3. Run installer and check "Add Python to PATH"

**Mac:**
```bash
brew install python3
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Step 2: Download This Project

**Option A: Using Git**
```bash
git clone https://github.com/Lucasvngpl/photo-organizer.git
cd photo-organizer
```

**Option B: Download ZIP**
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in that folder

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This might take a few minutes as it downloads TensorFlow (~500MB).

### Step 4: Prepare Test Photos

Create a test folder with some photos:

```bash
mkdir test_photos
# Copy some photos into test_photos/
```

Or use the setup script:

```bash
python setup.py
# Follow the prompts
```

### Step 5: Run It!

**Dry run first (doesn't move anything):**
```bash
python organizer.py test_photos --dry-run
```

**For real:**
```bash
python organizer.py test_photos
```

That's it! Check the `school_photos/` folder for organized images.

---

## For Hackathon Teams

### 30-Second Setup

```bash
# Clone and setup
git clone https://github.com/Lucasvngpl/photo-organizer.git
cd photo-organizer
pip install -r requirements.txt

# Test it
python demo.py
```

### What You Get

- ✅ Working ML classifier (EfficientNet)
- ✅ Photo organization logic
- ✅ Command-line interface
- ✅ Python API for custom integration
- ✅ Android adaptation guide

### Customize It

1. **Add more keywords** - Edit `config.py`, add to `HOMEWORK_KEYWORDS`
2. **Change threshold** - Edit `CONFIDENCE_THRESHOLD` in `config.py`
3. **Train on custom data** - Fine-tune the model (see TensorFlow docs)
4. **Build Android app** - Follow `ANDROID_GUIDE.md`

### Common Hackathon Extensions

**Idea 1: Auto-backup homework to cloud**
```python
from organizer import PhotoOrganizer
import google_drive_api

organizer = PhotoOrganizer('photos')
stats = organizer.organize_photos()

# Upload homework folder to Drive
upload_to_drive('school_photos/')
```

**Idea 2: OCR for searchable homework**
```python
from classifier import HomeworkImageClassifier
import pytesseract

classifier = HomeworkImageClassifier()
if classifier.is_homework_related('image.jpg')[0]:
    text = pytesseract.image_to_string('image.jpg')
    # Index text for search
```

**Idea 3: Study time tracker**
```python
# Count homework photos per day
import datetime
from organizer import PhotoOrganizer

organizer = PhotoOrganizer('photos')
results = organizer.classifier.classify_batch(images)

homework_today = sum(1 for _, is_hw, _, _ in results if is_hw)
print(f"Studied: {homework_today} items today")
```

---

## Troubleshooting

### "No module named tensorflow"
```bash
pip install tensorflow
```

### "pip not found"
Try `pip3` instead of `pip`:
```bash
pip3 install -r requirements.txt
```

### "Permission denied"
Add `--user` flag:
```bash
pip install --user -r requirements.txt
```

### Model download is slow
First run downloads ~30MB model. Subsequent runs are fast. Be patient!

### Out of memory
Use smaller batch size in `config.py`:
```python
BATCH_SIZE = 5  # Instead of 10
```

---

## Next Steps

1. ✅ **Test with real photos** - Use your actual photo library
2. ✅ **Customize keywords** - Add subject-specific terms
3. ✅ **Build Android app** - See `ANDROID_GUIDE.md`
4. ✅ **Add features** - OCR, cloud sync, statistics
5. ✅ **Win hackathon!** 🏆

---

## Getting Help

- 📖 Read the full [README.md](README.md)
- 🤖 Check [ANDROID_GUIDE.md](ANDROID_GUIDE.md) for mobile
- 🐛 Found a bug? Open an issue on GitHub
- 💡 Have an idea? Fork and contribute!

---

## Resources

- [TensorFlow Lite](https://www.tensorflow.org/lite)
- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [Android ML Kit](https://developers.google.com/ml-kit)
- [Python Image Processing](https://pillow.readthedocs.io/)

---

**Ready to organize!** 📚✨
