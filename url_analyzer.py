import re
def analyze_urls(email_text):

    urls = re.findall(r'https?://\S+', email_text)

    findings = []

    for url in urls:

        if url.startswith("http://"):
            findings.append("Non-HTTPS URL")

        if re.search(r'https?://\d+\.\d+\.\d+\.\d+', url):
            findings.append("IP-Based URL")

        if any(short in url for short in [
            "bit.ly",
            "tinyurl.com",
            "t.co"
        ]):
            findings.append("Shortened URL")

    return findings
