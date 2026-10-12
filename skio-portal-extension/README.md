# MUTO billing notice: Skio portal extension

A notice at the top of the Skio Customer Portal (v3). It shows at most one message, in this order:

| Priority | When | Message | Button |
|---|---|---|---|
| 1 | Last payment failed | Your last payment didn't go through. Update your card so your next delivery isn't held up. | Update card |
| 2 | Card expires within 30 days | Your card expires soon. Update it now so your protocol doesn't miss a month. | Update card |
| 3 | No backup card | Add a backup card. If your main card ever fails, we'll use this one, so you never miss a delivery. | Add backup card (dismissible for 30 days) |

Nothing shows when none apply, or when the billing status can't be read.

`previews/` has screenshots of each state on desktop and mobile.

## What's done

- Markup, brand styling (desktop and mobile), priority logic, and the 30-day expiry window.
- **Buttons** open the portal's own controls: the Billing section's **Edit** button for "Update card", and the backup payment button for "Add backup card". If neither can be found, they fall back to the Quick Action links in `CONFIG`.
- **Dismissing the backup-card message** hides it for 30 days in that browser. The payment messages can't be dismissed.
- **Preview mode:** add `?muto-billing=failed`, `?muto-billing=expiring` or `?muto-billing=nobackup` to the portal URL to see each state without real data.
- **Tested** in a mock portal page: each state shows the right message, the buttons click the portal's controls, nothing shows when all is well or the data is missing, and the dismiss is remembered.

## What the developer needs to do

### 1. Wire up `loadBillingStatus()`

It's the one function marked `TODO`. It should resolve to:

```js
{ paymentFailed: true|false, cardExpiry: 'YYYY-MM' | null, hasBackupCard: true|false }
```

or to `null` if the status can't be read (the notice then stays hidden).

Skio's public docs say extensions "run after the Customer Portal mounts", and that the portal shows the logged-in customer's subscriptions (the `storefrontUser`). They don't say how an extension reads that data. Ask Skio support (questions below), then pick one:

- **A. Skio exposes the customer to extensions** (a global, event or context object). This is the best option: map its fields to the shape above, in about 10 lines.
- **B. A small server endpoint** that holds the Skio API key and returns only these three values for the logged-in customer. It must check who the customer is on the server, for example with a Shopify app proxy signature (`logged_in_customer_id`). That only works if Skio's login also signs the customer into Shopify (Skio's Multipass option). **Never put a Skio or Shopify admin API key in the extension**: every customer can read it.
- **C. Read the portal page itself** (for example, a "payment failed" banner or the card details Skio already shows). This needs no API, but it breaks whenever Skio changes its page.

Useful data points from Skio's events (seen in Klaviyo): failed-payment events carry `statusContext: "DUNNING"`, `errorCode` and `numberOfFailedAttempts`. Card-expiry events carry `paymentMethodLastDigits` and `daysUntilExpiration`. Skio's API reference lists a `BackupPaymentMethod` on storefront users.

### 2. Check the button targets against the live portal

`CONFIG.billingSectionText`, `CONFIG.editButtonText` and `CONFIG.addBackupButtonText` find the portal's own buttons by their wording. Check them against the live portal and adjust if Skio's labels differ.

### 3. Add the fallback links

In Skio, go to Grow → Quick Actions → Create new action → Modify existing subscription → **Set backup payment method**. Create a link with link type "Skio" and paste it into `CONFIG.backupCardUrl`.

For card updates, the closest Quick Action ("Reset Payment Method") sends the customer an email from Shopify rather than opening a page. So `updateCardUrl` can stay empty, and the button just uses the portal's Edit button.

## Questions for Skio support

1. Can a CPv3 custom extension read the logged-in storefront user (subscriptions, payment methods, backup payment method)? If so, how: a global, an event or a context object? What are the exact field names?
2. Does that data include the card expiry month and year, and whether a subscription is currently in dunning?
3. Is there a supported way to open the portal's "update payment method" window from an extension (a route, a URL hash or an event)?
4. Does the Skio login also sign the customer into Shopify (Multipass)? This matters for option B.

## Installing

1. In Skio, go to Storefront → Customer Portal and confirm you're on **Customer Portal v3**.
2. In Portal Settings → Experience, turn on **Allow in-portal backup payment**.
3. **Before publishing, add your own email as a test email** in Skio. Without test emails, custom code changes go live for every customer at once.
4. Go to Branding → Layout → **Add custom extension**, paste `extension.html`, save, add it to the layout with **+**, and drag it to the top.
5. Log in with a test subscription and check each state, using the `?muto-billing=` preview first and then real data. Then remove the test email to go live.

Skio support won't write or debug extension code, so a developer needs to do steps 1–3 of "What the developer needs to do".
