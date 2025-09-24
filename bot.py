class PhishingAwarenessBot:
    def __init__(self):
        self.quiz_questions = [
            {
                "question": "You get an email from 'Bank XYZ' asking you to click a link to update your account. Is this phishing?",
                "choose": ["option1: yes", "option2: no", "option3: maybe", "option4: not sure"],
                "correct_answer": ["option1"],
                "explanation": {
                    "correct": "Great job! Legitimate banks don't send unsolicited links.",
                    "incorrect": "Actually, this is likely phishing. Always contact the bank directly."
                }
            },

            {
                "question": "How to check if a link is safe?",
                "choose": ["option1: click","option2: hover","option3: scan", "option4: none of the above"],
                "correct_answer": ["option2"],
                "explanation": {
                    "correct": "Correct! Hovering over links to preview URLs is a safe practice.",
                    "incorrect": "The safe way is to hover over the link to preview the URL without clicking!",
                }
            },

            {
                "question": "You receive an email from your CEO's personal Gmail account requesting an urgent wire transfer to a new vendor. It includes specific details about an ongoing project. What should you do?",
                "choose": ["option1: ignore", "option2: approve", "option3:  Verify via a separate channel (phone call/SMS) using known contact info", "option4: Contact the vendor directly"],
                "correct_answer": ["option3"],
                "explanation": {
                    "correct": "Always confirm financial requests through pre-established secure channels.",
                    "incorrect": "Sophisticated attackers research targets and spoof executive emails. Always confirm financial requests through pre-established secure channels.",
                }
            },

            {
                "question": "A parking garage email asks you to scan a QR code to renew your monthly pass. How risky is this?",
                 "choose": ["option1: Low Risk","option2: High Risk","option3: Medium Risk","option4: Not risky"],
                "correct_answer": ["option2"],
                "explanation": {
                    "correct": "Correct: High risk - QR codes can hide malicious links",
                    "incorrect": "Incorrect QR codes ('quishing') bypass traditional URL checks. Verify via the official app/website instead.",
                }
            
            },

            {
                "question":  "A login page has HTTPS and a valid certificate. Is it safe?",
                "choose": ["option1: yes", "option2: no","option3: maybe","option4: not sure"],
                "correct_answer": "option2",
                "explanation": {
                    "correct": " Not necessarily - phishing sites can have HTTPS too",
                    "incorrect": "Yes,HTTPS only encrypts data; it doesn’t validate the site’s legitimacy. Check the domain name carefully."
                }
            },

            {
                "question":  "A calendar invite from ‘IT Support’ pops up with a Zoom link for a ‘security update.’ What’s the best action?",
                "choose": ["option1: Delete the invite and report it to IT", "option2: maybe","option3: Join the meeting to stay updated","option4: not sure"],
                "correct_answer": "option1",
                "explanation": {
                    "correct": "Always delete the invite and report it to IT. Fake calendar events are a growing tactic. Legitimate IT teams won’t schedule unsolicited meetings via invites.",
                    "incorrect": "Fake calendar events are a growing tactic. Legitimate IT teams won’t schedule unsolicited meetings via invites."
            }
            },

            {
                "question": "A LinkedIn message from a recruiter at ‘Google’ asks you to download a ‘job application form’ from a tinyurl link. Is this safe?",
                "choose": ["option1: No", "option2: yes","option3: maybe","option4: not sure"],
                "correct_answer": "option1",
                "explanation": {
                    "correct": "No, fake job application forms are a growing tactic. Legitimate recruiters won’t send unsolicited job applications via tinyurl links.",
                    "incorrect": "Yes - recruiters often use LinkedIn.Always expand shortened links (e.g., with tools like CheckShortURL) before interacting."
            }
            },

            
]
        self.current_score = 0
        self.total_questions = len(self.quiz_questions)

    def welcome_message(self):
        message = """Hello! I'm your cybersecurity assistant here to help you learn about phishing and stay safe online. How can I assist you today?

Available options:
1. What is phishing?
2. How to spot phishing?
3. Phishing examples
4. Take a quiz
5. Report phishing
6. Safety tips
7. Something else

Please enter the number or type your question:"""
        return message

    def handle_response(self, user_input):
        user_input = user_input.lower().strip()
        
        if user_input in ['1', 'what is phishing']:
            return self.what_is_phishing()
        elif user_input in ['2', 'how to spot phishing']:
            return self.spot_phishing()
        elif user_input in ['3', 'phishing examples']:
            return self.phishing_examples()
        elif user_input in ['4', 'take a quiz']:
            return self.start_quiz()
        elif user_input in ['5', 'report phishing']:
            return self.report_phishing()
        elif user_input in ['6', 'safety tips']:
            return self.safety_tips()
        elif user_input in ['7', 'something else']:
            return self.handle_other_queries()
        else:
            return "I'm focused on phishing awareness. Please choose an option from above, or ask about examples/quizzes!"

    def what_is_phishing(self):
        return """Phishing is a type of cyber attack where cybercriminals attempt to deceive individuals into providing sensitive information, such as usernames, passwords, credit card details, or other personal data. This is typically done by pretending to be a trustworthy entity, often through emails, messages, or fake websites. The goal is to trick the victim into revealing information that can then be used for fraudulent activities like identity theft, financial fraud, or unauthorized access to accounts.

How Phishing Works:
Deceptive Email or Message: The attacker sends an email, text message, or social media message that looks like it's from a legitimate source, such as a bank, online service, or social media platform.
Urgent or Threatening Language: The message often contains an urgent request or threat to create a sense of panic. For example, the victim might be told that their account is compromised, and they need to act quickly.
Fake Link or Attachment: The message includes a link that looks like it leads to a legitimate website or a malicious attachment. The link often contains a slight variation in the URL, which the victim may not notice at first glance (e.g., "www.paypal-support.com" instead of "www.paypal.com").
Tricking the Victim: If the victim clicks on the link or opens the attachment, they are either taken to a fake website that asks them to enter personal information (such as login credentials or credit card details) or they may inadvertently download malware to their device.

Example of Phishing:

Scenario: You receive an email claiming to be from your bank.
Subject: Urgent! Your account has been locked.
Email Body:
Dear Customer,
We have detected suspicious activity in your bank account and have temporarily locked it for your protection.
To unlock your account, you must confirm your identity by following the link below:
Unlock My Account
http:/Sbi.co.in
Please complete this process within 24 hours to avoid further action.
Thank you for choosing [SBI].


What Happens:
The victim is scared by the "urgent" message, thinking their account is at risk.
The link in the email looks like it’s from the bank, but the URL is slightly altered (e.g., it might say "bank-secure-logon.com" instead of the actual bank's website). It could also use an address that closely resembles the bank’s actual website, but with small differences, making it easy for the victim to overlook.
When the victim clicks the link, they are taken to a fake website that looks identical to the real banking website. They might be asked to enter their username, password, or credit card details.
If the victim enters this sensitive information, the attacker now has access to the victim’s bank account or financial data.
Signs of Phishing:
Suspicious sender: The sender's email address may look odd or unfamiliar.
Generic greetings: Instead of addressing you by name, phishing emails might use a generic greeting like "Dear customer" or "Dear user."
Urgency or threats: Phishing emails often include a sense of urgency, such as a deadline to verify your account or else it will be locked.
Suspicious links: Hover your mouse over the link to check the URL. If it looks strange or doesn't match the official website, it’s likely phishing.
Spelling and grammar errors: Many phishing emails have noticeable spelling and grammar mistakes.
How to Protect Yourself from Phishing:
Don’t click on suspicious links: Always verify the authenticity of links before clicking.
Check email addresses: Verify the sender's email address, especially if it's unfamiliar.
Enable two-factor authentication: This adds an extra layer of security to your accounts.
Use anti-phishing software: Many email services and web browsers have built-in protections to warn you about phishing websites.
Verify directly: If you receive an unexpected email from a company you trust, contact them directly using their official contact details (not the ones provided in the email)."""


    def spot_phishing(self):
        return """
1.Check the Email Address:
                    Phishing emails often come from addresses that appear similar to legitimate ones but with slight differences.
                    For example, instead of support@bank.com, it might come from support@bank-secure.com.
2.Suspicious Links:
             Hover over the links in the email without clicking. If the URL looks suspicious, it may be a phishing attempt. For example, instead of www.amazon.com, the link could be www.amaz0n.com (note the "0" instead of an "o").

3.Generic Greeting:
             Phishing emails often use a generic greeting such as “Dear Customer” or “Dear User” rather than addressing you by name. A legitimate company typically knows your name and uses it in their correspondence.

4.Urgent or Threatening Language:
             Phishing emails often create a sense of urgency, such as “Your account will be locked unless you act now!” or “Immediate action required!”

5.Attachments:
             Be cautious with email attachments. Phishing emails may ask you to open an attachment that could contain malware or viruses. Only open attachments if you’re sure they come from a trusted source.

6.Poor Grammar and Spelling:
            Many phishing emails contain spelling mistakes and poor grammar. Official emails from reputable organizations are generally well-written.

7.Inconsistent Design:
            Phishing emails often have broken images, strange formatting, or incorrect logos, unlike professionally-designed emails from legitimate companies.
"""

    def phishing_examples(self):
        return """Common Phishing Examples:

1. Email Phishing Example:
This is the most common form of phishing, where attackers send deceptive emails pretending to be from a trusted source.

Phishing Email Example:

Subject: Important: Your PayPal Account has been Restricted!

Email Body:

Dear [Golmu],
We’ve detected unusual activity in your PayPal account, and as a result, your account has been temporarily restricted for your protection.
To restore your account, please follow the link below and verify your identity:
Verify Now
http://www.paypal.com/my/account

Failure to act within 48 hours may result in permanent suspension of your account.
Regards,
PayPal Security Team

Why It’s Phishing:

Generic Greeting: It says "Dear [Your Name]" but doesn’t include your full name or any personal information.
Suspicious Link: The link doesn’t lead to the official paypal.com site, but a fake URL designed to look similar.
Urgency: The "48 hours" deadline creates pressure to click quickly without thinking.
Threat of Suspension: Phishing emails often use threats to force quick action.

2. Spear-Phishing Example:
Spear-phishing is a more targeted attack where the attacker uses personal information to craft a believable message. This makes spear-phishing much more convincing than regular phishing.

Phishing Email Example:

Subject: Invoice Attached – [Company Name] – Payment Due

Email Body:

Hi [Vivek],

I hope this email finds you well. Please find the invoice for this month’s payment attached. Kindly review it and make the payment as soon as possible.
Let me know if you have any questions.

Best regards,
[Rajeev]
[playstation]

Why It’s Phishing:

Personalized: The email uses your name, your company’s name, and the name of a trusted colleague. This makes it look legitimate.
Malicious Attachment: The invoice is likely an attachment containing malware or ransomware.
Pretext: The attacker assumes the role of a trusted colleague and uses business context to trick the victim.

3. Smishing (SMS Phishing) Example:
Phishing attacks aren’t limited to email. Smishing involves phishing attempts via text messages (SMS).

SMS Phishing Example:

Alert: Your bank account has been compromised!
To secure your account, click here to verify: [/http:/Sbi.co.in/verify]. Failure to do so will result in loss of funds.

[SBI] Security Team

Why It’s Phishing:

Urgency: The message creates a sense of panic by claiming that your account is compromised.
Suspicious Link: The link takes you to a fake website designed to steal your banking details.
Unsolicited Text: Legitimate banks would never send unsolicited text messages with urgent requests for action.

4. Voice Phishing (Vishing) Example:
Vishing, or voice phishing, happens when attackers use phone calls to manipulate victims into revealing sensitive information.

Vishing Call Example:

Phone Call:
"Hi, this is Shalini from your bank. We noticed unusual activity on your account and need to verify your identity to prevent unauthorized access. 
Please provide your account number and the PIN to confirm your identity."

Why It’s Phishing:

Impersonation: The attacker claims to be from the bank but doesn’t provide verifiable information.
Request for Sensitive Info: Legitimate banks will never ask for your account number, PIN, or passwords over the phone.
No Verification: The caller may push you to act quickly, making it harder to verify their identity.

5. Phishing via Fake Social Media Pages
Attackers often create fake social media profiles or impersonate trusted brands to trick people into revealing their personal information or credentials.

Fake Social Media Phishing Example:

A fake Facebook page or Instagram profile that impersonates a well-known company (like Apple, Netflix, or Amazon).
The page may claim that the user has won a prize, but they need to verify their personal information to claim it.
Example message: "Congratulations! You've won a free iPhone! To claim your prize, click the link below and fill out the form."

Why It’s Phishing:

Fake Offers: Phishing often involves fake giveaways or prizes to lure victims into providing personal details.
Suspicious Links: The links will take you to a fake website where you’re asked to input sensitive information like your address, phone number, and credit card details.

6. Business Email Compromise (BEC) Example.
In Business Email Compromise (BEC) attacks, cybercriminals impersonate a company executive to deceive employees into transferring money or sensitive data.

BEC Phishing Example:

Subject: Urgent Payment Request – Confidential

Email Body:

Hi [Priyanshu],

Please process the payment to the vendor below immediately. I need it to be completed by the end of the day for a critical project.

Vendor Name: Cocane supplies
Amount: $50,000

Let me know once it's done.

Best regards,
[Vedant]
[Mankind]

Why It’s Phishing:

Impersonation: The attacker impersonates a high-level executive (like the CEO).
Urgency: The email demands quick action to process a large payment, hoping to catch the victim off guard.
Unusual Request: The email could be legitimate if the CEO commonly makes such requests, but the payment request could be fraudulent.


"""




    def start_quiz(self):
        if not hasattr(self, 'current_question'):
            self.current_question = 0
            self.current_score = 0
        
        if self.current_question >= len(self.quiz_questions):
            return self.finish_quiz()
        
        question = self.quiz_questions[self.current_question]
        return f"Question {self.current_question + 1}/{self.total_questions}:\n{question['question']}"

    def check_answer(self, answer):
        if not hasattr(self, 'current_question'):
            return "Please start the quiz first!"
        
        question = self.quiz_questions[self.current_question]
        answer = answer.lower().strip()
        
        if answer in question['correct_answer']:
            self.current_score += 1
            response = question['explanation']['correct']
        else:
            response = question['explanation']['incorrect']
        
        self.current_question += 1
        
        if self.current_question >= len(self.quiz_questions):
            return response + "\n\n" + self.finish_quiz()
        else:
            next_question = self.quiz_questions[self.current_question]
            return f"{response}\n\nNext question:\n{next_question['question']}"

    def finish_quiz(self):
        score_percentage = (self.current_score / self.total_questions) * 100
        message = f"""Quiz completed!
Your score: {self.current_score}/{self.total_questions} ({score_percentage:.0f}%)

"""
        if score_percentage == 100:
            message += " Perfect score! You're a phishing awareness expert!"
        elif score_percentage >= 70:
            message += " Good job! You're getting savvy at spotting scams!"
        else:
            message += "Keep learning! Review our tips and try again."
        
        # Reset quiz state
        delattr(self, 'current_question')
        self.current_score = 0
        
        return message + "\n\nWould you like to:\n1. Try another quiz\n2. Review safety tips\n3. Return to main menu"

    def report_phishing(self):
        return """To report phishing attempts:

1. Forward suspicious emails to your IT department
2. Use your email client's built-in reporting (Gmail/Outlook)
3. Send to reportphishing@apwg.org
4. Report to your country's cybersecurity center

Remember: Reporting helps protect others!

"""

    def safety_tips(self):
        return """Essential Safety Tips:

 Enable multi-factor authentication (MFA)
 Keep software and systems updated
 Verify suspicious messages via official channels
 Never click links in unsolicited emails
 Always check email sender addresses
 Be cautious with unexpected requests

Latest Trend Alert: Recent spike in Amazon delivery notification phishing scams!

"""

    def handle_other_queries(self):
        return """I can help you with:

 Understanding different types of phishing
 Identifying latest phishing trends
 Mobile phishing (smishing)
 Specific scam examples
 Advanced protection methods

Please let me know what interests you, or choose from the main menu options."""

# Create and run the chatbot
if __name__ == "__main__":
    bot = PhishingAwarenessBot()
    print(bot.welcome_message())
    
    while True:
        try:
            user_input = input("\nYour response: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\nStay safe online—always think before you click! Return anytime for more tips.")
                break
                
            response = bot.handle_response(user_input)
            print("\n" + response)
            
        except KeyboardInterrupt:
            print("\n\nStay safe online—always think before you click! Return anytime for more tips.")
            break
        except Exception as e:
            print("\nI apologize for the confusion. Let's start over with the main menu.")
            print(bot.welcome_message())