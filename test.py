from dotenv import load_dotenv
load_dotenv()   # MUST be before any core/ imports

from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarize import summarize, generate_title
from core.extractor import extract_action_items, extract_key_decisions, extract_questions


source = "https://youtu.be/_Q-e_nczWqM?si=uKWkjPr3EAIveSbJ"
language = "english"   # "english" → Whisper, "hinglish" → Sarvam



chunks = process_input(source)


transcript = transcribe_all(chunks, language=language)
print("\n" + "=" * 60)
print("📝 TRANSCRIPT")
print("=" * 60)
print(transcript[:500] + "..." if len(transcript) > 500 else transcript)


title = generate_title(transcript)
summary = summarize(transcript)

print("\n" + "=" * 60)
print(f"📌 TITLE: {title}")
print("=" * 60)
print("\n📋 SUMMARY")
print("-" * 60)
print(summary)



action_items = extract_action_items(transcript)
decisions = extract_key_decisions(transcript)
questions = extract_questions(transcript)

print("\n" + "=" * 60)
print("✅ ACTION ITEMS")
print("=" * 60)
print(action_items)

print("\n" + "=" * 60)
print("🔑 KEY DECISIONS")
print("=" * 60)
print(decisions)

print("\n" + "=" * 60)
print("❓ OPEN QUESTIONS")
print("=" * 60)
print(questions)

# ==========Flow============
  #                  YouTube URL / Audio File
  #                             │
  #                             ▼
  #                   process_input(source)
  #                             │
  #         ┌───────────────────┴────────────────────┐
  #         │                                        │
  #  Download (if URL)                   Convert (if local file)
  #         │                                        │
  #         └───────────────────┬────────────────────┘
  #                             ▼
  #                        WAV Audio
  #                             │
  #                             ▼
  #                    Split into Chunks
  #                             │
  #                             ▼
  #                 [chunk1, chunk2, chunk3...]
  #                             │
  #                             ▼
  #            transcribe_all(chunks, language)
  #                             │
  #                             ▼
  #                 Complete Transcript
  #                             │
  #         ┌───────────────────┼────────────────────┐
  #         ▼                   ▼                    ▼
  # generate_title()      summarize()        extractor.py
  #         │                   │                    │
  #         │                   │          ┌─────────┼──────────┐
  #         │                   │          ▼         ▼          ▼
  #         │                   │     Action    Decisions   Questions
  #         │                   │
  #         └──────────────┬────┴──────────────────────────────┘
  #                        ▼
  #                Final Meeting Report
  #                        │
  #                        ▼
  #       Title + Summary + Action Items + Decisions + Questions