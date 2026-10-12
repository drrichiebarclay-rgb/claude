"""Branded Klaviyo templates for MUTO's failed-payment and card-expiry flows.

Writes one HTML file per email into this folder. Run: python3 build.py
Uses Skio event data: {{ event.manageSubscriptionUrl }}, {{ event.paymentMethodLastDigits }}.
"""
INK, BG, MUTED, RULE = "#162f31", "#f4f2ee", "#5b6b6c", "#d9dcd8"

def page(preheader, heading, paras, button, url, footnote):
    body = "".join(f'<p style="margin:0 0 16px;font-size:16px;line-height:1.55;color:{INK};">{p}</p>' for p in paras)
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MUTO</title></head>
<body style="margin:0;padding:0;background:{BG};">
<div style="display:none;max-height:0;overflow:hidden;">{preheader}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{BG};"><tr><td align="center" style="padding:32px 16px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#ffffff;border-radius:20px;">
<tr><td style="padding:36px 36px 8px;font-family:Helvetica,Arial,sans-serif;">
<div style="font-size:15px;font-weight:700;letter-spacing:.28em;color:{INK};">MUTO</div>
</td></tr>
<tr><td style="padding:16px 36px 8px;font-family:Helvetica,Arial,sans-serif;">
<h1 style="margin:0 0 20px;font-size:28px;line-height:1.2;font-weight:500;letter-spacing:-.01em;color:{INK};">{heading}</h1>
<p style="margin:0 0 16px;font-size:16px;line-height:1.55;color:{INK};">Hi {{{{ first_name|default:'there' }}}},</p>
{body}
</td></tr>
<tr><td style="padding:8px 36px 28px;font-family:Helvetica,Arial,sans-serif;">
<a href="{url}" style="display:inline-block;padding:15px 28px;border-radius:999px;background:{INK};color:#ffffff;font-size:16px;font-weight:500;text-decoration:none;">{button}</a>
</td></tr>
<tr><td style="padding:20px 36px 32px;border-top:1px solid {RULE};font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:1.5;color:{MUTED};">
{footnote}<br>Questions? Just reply to this email, or write to <a href="mailto:hello@mutolongevity.com" style="color:{INK};">hello@mutolongevity.com</a>.
</td></tr>
</table>
<p style="margin:20px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:12px;line-height:1.5;color:{MUTED};">{{{{ organization.name }}}} · {{{{ organization.full_address }}}}<br>{{% unsubscribe 'Unsubscribe' %}}</p>
</td></tr></table>
</body></html>
"""

URL = "{{ event.manageSubscriptionUrl|default:'https://muto.co/account' }}"
SECURE = "Your card details are held securely by Shopify. We never see or store them."

EMAILS = {
    "01_payment_retry": dict(
        preheader="No action needed. We'll try again in a few days.",
        heading="We couldn't take this month's payment",
        paras=["Your bank turned down this month's payment for your MUTO plan. This usually means the account was a little short on the day.",
               "<strong>You don't need to do anything.</strong> We'll try again automatically in a few days, and your protocol carries on as normal once it goes through.",
               "If you'd rather use a different card, you can change it in under a minute."],
        button="Use a different card", footnote=SECURE),
    "02_update_card": dict(
        preheader="Update your card so your next delivery isn't held up.",
        heading="Your last payment didn't go through",
        paras=["We tried to take this month's payment for your MUTO plan, but your card was declined or is no longer active.",
               "Update your card so your next delivery isn't held up. It takes under a minute."],
        button="Update card", footnote=SECURE),
    "03_on_hold": dict(
        preheader="Your next delivery is waiting on a card update.",
        heading="Your protocol is on hold",
        paras=["We still haven't been able to take payment for your MUTO plan, so your next delivery is on hold.",
               "Update your card and we'll pick up where you left off.",
               "Want to pause instead? You can do that from the same page."],
        button="Update card", footnote=SECURE),
    "04_card_expiring": dict(
        preheader="Update it now so your protocol doesn't miss a month.",
        heading="Your card expires soon",
        paras=["The card ending {{ event.paymentMethodLastDigits }} on your MUTO plan expires soon.",
               "Update it now so your protocol doesn't miss a month."],
        button="Update card", footnote=SECURE),
}

for name, e in EMAILS.items():
    open(f"{name}.html", "w").write(page(url=URL, **e))
    print("wrote", name)
