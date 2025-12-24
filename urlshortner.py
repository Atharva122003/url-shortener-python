#python -m pip install pyshorteners (to install the module pyshorteners)
import pyshorteners

try:
    #python -m pip install pyperclip(to install module pyperclip)
    import pyperclip
    clipboard_available = True
except ImportError:
    clipboard_available = False

def shorten_url(url):
    try:
        short = pyshorteners.Shortener().tinyurl.short(url)
        print(f"\nShortened URL: {short}")
        if clipboard_available:
            pyperclip.copy(short)
            print("✅ URL copied to clipboard!")
        return short
    except Exception as e:
        print(f"❌ Error shortening URL: {e}")
        return None

def main():
    print("🔗 Python URL Shortener")
    if not clipboard_available:
        print("Tip: Install 'pyperclip' to copy URLs to clipboard automatically: pip install pyperclip\n")

    while True:
        url = input("Enter URL (or 'exit' to quit): ").strip()
        if url.lower() == 'exit':
            print("Goodbye! 🔗")
            break
        elif url.startswith("http://") or url.startswith("https://"):
            shorten_url(url)
        else:
            print("❌ Invalid URL! Make sure it starts with http:// or https://\n")

if __name__ == "__main__":
    main()
