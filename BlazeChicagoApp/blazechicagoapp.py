from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
import os
import smtplib
from email.mime.text import MIMEText

class BlazeChicagoApp(App):
    def build(self):
        # ✅ Set Background Color to White
        Window.clearcolor = (1, 1, 1, 1)  # White Background

        # ✅ Main Layout (Vertical)
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # ✅ LOGO: Load image from absolute path
        logo_path = os.path.abspath("logo.png")  # Ensure correct path
        if os.path.exists(logo_path):
            logo = Image(source=logo_path, size_hint=(None, None), size=(250, 250), pos_hint={"center_x": 0.5})
        else:
            logo = Label(text="🚫 Logo Not Found!", font_size=20, color=(1, 0, 0, 1))

        # ✅ Business Info
        title = Label(text="Welcome to Blaze Chicago", font_size=32, bold=True, color=(0, 0, 0, 1))
        hours = Label(text="Business Hours\nMonday - Saturday: 10 AM – 8 PM\nSunday: 10 AM – 6 PM",
                      font_size=20, color=(0, 0, 0, 1), size_hint=(1, None), height=80)
        phone = Label(text="Call Us: (312) 399-1172", font_size=20, color=(0, 0, 1, 1), size_hint=(1, None), height=50)

        # ✅ Form Layout
        form_layout = BoxLayout(orientation="vertical", spacing=15, size_hint=(1, None), height=300)
        self.name_input = TextInput(hint_text="Enter Your Name", font_size=18, size_hint_y=None, height=50)
        self.phone_input = TextInput(hint_text="Enter Your Phone Number", font_size=18, size_hint_y=None, height=50)
        self.item_input = TextInput(hint_text="Enter Desired Item", font_size=18, size_hint_y=None, height=50)

        # ✅ Confirmation Label (Initially Hidden)
        self.confirmation_label = Label(text="", font_size=20, color=(0, 0.5, 0, 1), bold=True)

        submit_btn = Button(
    text="Submit Order Request",
    font_size=24,
    size_hint_y=None,
    height=60,
    background_color=(0.502, 0.851, 0.973, 1),  # ✅ Converted #80d9f8 to Kivy's RGBA format
    bold=True,
    on_press=self.submit_order
)

        # ✅ Add Form Widgets
        form_layout.add_widget(Label(text="Order Request Form", font_size=24, bold=True, color=(0, 0, 0, 1)))
        form_layout.add_widget(self.name_input)
        form_layout.add_widget(self.phone_input)
        form_layout.add_widget(self.item_input)
        form_layout.add_widget(submit_btn)
        form_layout.add_widget(self.confirmation_label)

        # ✅ Add All Widgets to Layout
        main_layout.add_widget(logo)  # ✅ Logo now properly handled
        main_layout.add_widget(title)
        main_layout.add_widget(hours)
        main_layout.add_widget(phone)
        main_layout.add_widget(Label(size_hint_y=None, height=20))  # Add extra spacing
        main_layout.add_widget(form_layout)

        return main_layout

    def send_order_email(self, name, phone, item):
        """✅ Sends an email with the order details."""
        sender_email = "shawn.iconicexotic@gmail.com"  # 🔹 Your email
        sender_password = "tzdf kclo mdqm knly"  # 🔹 Use an App Password
        recipient_email = "shawn.iconicexotic@gmail.com"  # 🔹 Your email to receive orders

        subject = f"🚀 New Order Request from {name}"
        body = f"📌 Name: {name}\n📞 Phone: {phone}\n🛒 Item Requested: {item}\n\n✅ Please follow up with the customer."

        msg = MIMEText(body)
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)  # 🔹 Change for Outlook/Yahoo
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"❌ Email failed: {e}")
            return False

    def submit_order(self, instance):
        """✅ Handles the order form submission."""
        name = self.name_input.text.strip()
        phone = self.phone_input.text.strip()
        item = self.item_input.text.strip()

        if name and phone and item:
            if self.send_order_email(name, phone, item):
                self.confirmation_label.text = "✅ Order submitted! We will contact you shortly."
                self.confirmation_label.color = (0, 1, 0, 1)  # Green Text
                self.name_input.text = ""
                self.phone_input.text = ""
                self.item_input.text = ""
            else:
                self.confirmation_label.text = "❌ Order failed! Try again."
                self.confirmation_label.color = (1, 0, 0, 1)  # Red Text
        else:
            self.confirmation_label.text = "❌ Please fill in all fields!"
            self.confirmation_label.color = (1, 0, 0, 1)  # Red Text

# ✅ Run the App
if __name__ == "__main__":
    BlazeChicagoApp().run()
