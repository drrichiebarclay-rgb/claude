"""Cart drawer (snippets/cart-drawer.liquid): NAD first, then gifts in a fixed order; reassurance
for subscriptions; savings and cost-per-day lines; "Checkout · £total"; one trust row.

- Order: NAD (and anything not listed) first, then creatine, socks, bottle, ebook, jar, Garmin last.
- Removed: the reviews.io box (both states) and the free-shipping bar.
- Subscription in the cart: three lines at the top (90 days or every payment back, skip/pause/cancel, 4.8/5).
- NAD line: grey "Replaces 5 supplements · £x a day" under the title (no per-day on one-time),
  green ticked "You save £x every 3 months / every month, ongoing" on subscriptions.
- Free lines (the welcome kit) leave the table for an 8hours-style list: "Your free welcome gifts (n)",
  thumbnail, name, value struck through, Free. Subtotal reads struck total · total · Save £x, where the
  struck total is the sum of the struck prices shown above.
- Quantity inputs are keyed by line (updates[key]), so the new order can't move quantities at checkout.
- No price under the title (the right-hand column has it).
- Button: "Checkout · £150" from the live cart total. Under the payment icons: secure checkout ·
  cancel anytime · 90-day guarantee.

Usage: python3 apply_cart.py <in cart-drawer.liquid> <out cart-drawer.liquid>
"""
import sys

STYLE = """
<style>
  .mc-cart-sub{margin:4px 0 0;padding:14px 16px;border-radius:12px;background:rgba(36,34,35,.06);color:#242223;font-size:14px;line-height:1.4}
  .mc-cart-sub p{margin:0}
  .mc-cart-sub p:first-child{font-weight:600}
  .mc-cart-sub p + p{margin-top:4px}
  .mc-cart-sub__stars{letter-spacing:.08em}
  .mc-cart-line{display:block;margin:6px 0 0;font-size:13px;line-height:1.35}
  .mc-cart-line--per-day{color:rgba(36,34,35,.65)}
  .mc-cart-line--save{display:flex;align-items:flex-start;gap:6px;color:#1f7a3d;font-weight:500}
  .mc-cart-line--save svg{flex:0 0 12px;width:12px;height:12px;margin-top:.2em}
  .mc-cart-gifts{margin:4px 0 0;padding:18px 0 4px;border-top:1px solid rgba(36,34,35,.12)}
  .mc-cart-gifts__title{margin:0 0 10px;font-size:16px;font-weight:600;color:#242223}
  .mc-cart-gifts__list{display:grid;gap:8px;margin:0;padding:0;list-style:none}
  .mc-cart-gift{display:flex;align-items:center;gap:12px;margin:0;padding:8px 14px 8px 8px;border-radius:12px;background:rgba(36,34,35,.05);font-size:14px;line-height:1.3;color:#242223}
  .mc-cart-gift__img{flex:0 0 40px;width:40px;height:40px;border-radius:8px;object-fit:cover}
  .mc-cart-gift__name{flex:1 1 auto;min-width:0;font-weight:500}
  .mc-cart-gift__was{color:rgba(36,34,35,.5);white-space:nowrap}
  .mc-cart-gift__free{font-weight:600;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
  .mc-totals{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:6px 12px}
  .mc-totals .totals__total{margin:0}
  .mc-totals__value{display:flex;flex-wrap:wrap;align-items:center;justify-content:flex-end;gap:6px 10px;margin:0}
  .mc-totals__was{color:rgba(36,34,35,.5);font-size:16px}
  .mc-totals__now{font-size:20px;font-weight:600;color:#242223}
  .mc-totals__save{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;background:#242223;color:#fff;font-size:13px;font-weight:600;white-space:nowrap}
  .mc-totals__save svg{width:11px;height:9px}
  .mc-cart-trust{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:4px 10px;margin:12px 0 0;padding:0;list-style:none;font-size:12px;line-height:1.3;color:#242223;text-align:center}
  .mc-cart-trust li{display:flex;align-items:center;gap:5px;margin:0}
  .mc-cart-trust li + li::before{content:"\\00b7";margin-right:5px;opacity:.6}
  .mc-cart-trust svg{width:12px;height:12px;flex:0 0 12px}
</style>
"""

SUB_NOTE = """
        {%- liquid
          assign mc_has_sub = false
          for mc_i in cart.items
            if mc_i.selling_plan_allocation
              assign mc_has_sub = true
              break
            endif
          endfor
        -%}
        {%- if mc_has_sub -%}
          <div class="mc-cart-sub">
            <p>Feel the difference in 90 days – or get every payment back.</p>
            <p>Skip, pause or cancel online anytime.</p>
            <p><span class="mc-cart-sub__stars" aria-hidden="true">★★★★★</span> 4.8/5<span class="visually-hidden"> from customer reviews</span></p>
          </div>
        {%- endif -%}
"""

LOOP_OPEN = """{%- for item in cart.items -%}
                      {%- liquid
                        assign is_giveaway_product = false"""
LOOP_OPEN_NEW = """{%- comment -%}
                      Cart order: NAD (and anything not listed) first, then the gifts — creatine,
                      socks, bottle, ebook, jar — with the Garmin entry last. One pass per place;
                      item.index still names each line, so updates and removals are unaffected.
                    {%- endcomment -%}
                    {%- for mc_pass in (1..7) -%}
                    {%- for item in cart.items -%}
                      {%- liquid
                        assign mc_h = item.product.handle
                        assign mc_rank = 1
                        if mc_h contains 'garmin'
                          assign mc_rank = 7
                        elsif mc_h contains 'creatine'
                          assign mc_rank = 2
                        elsif mc_h contains 'socks'
                          assign mc_rank = 3
                        elsif mc_h contains 'bottle'
                          assign mc_rank = 4
                        elsif mc_h contains 'ebook'
                          assign mc_rank = 5
                        elsif mc_h contains 'jar'
                          assign mc_rank = 6
                        endif
                        if mc_rank != mc_pass
                          continue
                        endif
                        # Free lines (the welcome kit) are listed under the table, not as rows
                        if item.final_line_price == 0 or item.properties._Giveaway_Sample == 'Free Giveaway'
                          continue
                        endif
                        assign is_giveaway_product = false"""
LOOP_CLOSE = """                    {%- endfor -%}
                  </tbody>"""
LOOP_CLOSE_NEW = """                    {%- endfor -%}
                    {%- endfor -%}
                  </tbody>"""

NAME = """                            {{- item.product.title | escape -}}
                          </a>
"""
NAME_NEW = NAME + """
                          {%- if item.product.handle contains 'nad-cellular-complex' -%}
                            {%- liquid
                              assign mc_alloc = item.selling_plan_allocation
                              assign mc_plan = mc_alloc.selling_plan.name | downcase
                              assign mc_days = 30
                              assign mc_months = 1
                              assign mc_every = 'every month'
                              if mc_plan contains '3-month'
                                assign mc_days = 90
                                assign mc_months = 3
                                assign mc_every = 'every 3 months'
                              endif
                            -%}
                            <span class="mc-cart-line mc-cart-line--per-day">
                              Replaces 5 supplements
                              {%- if mc_alloc %} · {{ mc_alloc.price | times: 1.0 | divided_by: mc_days | round | money_without_trailing_zeros }} a day{% endif -%}
                            </span>
                            {%- if mc_alloc -%}
                              {%- liquid
                                assign mc_was = mc_alloc.compare_at_price
                                unless mc_was > mc_alloc.price
                                  assign mc_was = item.variant.compare_at_price | default: item.variant.price | times: mc_months
                                endunless
                                assign mc_save = mc_was | minus: mc_alloc.price | times: item.quantity
                              -%}
                              {%- if mc_save > 0 -%}
                                <span class="mc-cart-line mc-cart-line--save">
                                  <svg viewBox="0 0 12 10" aria-hidden="true"><path fill="currentColor" d="M0 5.2 1.6 3.8 4.6 6.4 10.6.2 12 1.6 4.6 9.2z"/></svg>
                                  You save {{ mc_save | money_without_trailing_zeros }} {{ mc_every }}, ongoing
                                </span>
                              {%- endif -%}
                            {%- endif -%}
                          {%- endif -%}
"""

GIFTS = """                </table>
                {%- liquid
                  assign mc_gifts = 0
                  for item in cart.items
                    if item.final_line_price == 0 or item.properties._Giveaway_Sample == 'Free Giveaway'
                      assign mc_gifts = mc_gifts | plus: item.quantity
                    endif
                  endfor
                -%}
                {%- if mc_gifts > 0 -%}
                  <div class="mc-cart-gifts">
                    <p class="mc-cart-gifts__title">Your free welcome gifts ({{ mc_gifts }})</p>
                    <ul class="mc-cart-gifts__list" role="list">
                      {%- for mc_pass in (1..7) -%}
                        {%- for item in cart.items -%}
                          {%- liquid
                            unless item.final_line_price == 0 or item.properties._Giveaway_Sample == 'Free Giveaway'
                              continue
                            endunless
                            assign mc_h = item.product.handle
                            assign mc_rank = 1
                            if mc_h contains 'garmin'
                              assign mc_rank = 7
                            elsif mc_h contains 'creatine'
                              assign mc_rank = 2
                            elsif mc_h contains 'socks'
                              assign mc_rank = 3
                            elsif mc_h contains 'bottle'
                              assign mc_rank = 4
                            elsif mc_h contains 'ebook'
                              assign mc_rank = 5
                            elsif mc_h contains 'jar'
                              assign mc_rank = 6
                            endif
                            if mc_rank != mc_pass
                              continue
                            endif
                            assign mc_val = item.variant.compare_at_price | default: 0 | times: item.quantity
                            if item.original_line_price > mc_val
                              assign mc_val = item.original_line_price
                            endif
                          -%}
                          <li class="mc-cart-gift">
                            {%- if item.image -%}
                              <img class="mc-cart-gift__img" src="{{ item.image | image_url: width: 120 }}" alt="" loading="lazy" width="40" height="40">
                            {%- endif -%}
                            <span class="mc-cart-gift__name">{% if item.quantity > 1 %}{{ item.quantity }} × {% endif %}{{ item.product.title | escape }}</span>
                            {%- if mc_val > 0 -%}
                              <s class="mc-cart-gift__was"><span class="visually-hidden">Worth </span>{{ mc_val | money }}</s>
                            {%- endif -%}
                            <span class="mc-cart-gift__free">Free</span>
                          </li>
                        {%- endfor -%}
                      {%- endfor -%}
                    </ul>
                  </div>
                {%- endif -%}
"""

# Subtotal: the struck figure is the sum of the struck prices shown above (each line's old price,
# each gift's value), so every number at the bottom can be traced to one in the cart.
TOTALS_NEW = """<div class="totals mc-totals" role="status">
            <h2 class="totals__total">{{ 'sections.cart.estimated_total' | t }}</h2>
            {%- liquid
              assign mc_was_total = 0
              for item in cart.items
                assign mc_cmp = item.variant.compare_at_price | default: 0 | times: item.quantity
                if item.final_line_price == 0 or item.properties._Giveaway_Sample == 'Free Giveaway'
                  assign mc_line = item.original_line_price
                  if mc_cmp > mc_line
                    assign mc_line = mc_cmp
                  endif
                elsif item.original_line_price != item.final_line_price
                  assign mc_line = item.original_line_price
                elsif mc_cmp > item.original_line_price
                  assign mc_line = mc_cmp
                else
                  assign mc_line = item.final_line_price
                endif
                assign mc_was_total = mc_was_total | plus: mc_line
              endfor
              assign mc_saved = mc_was_total | minus: cart.total_price
            -%}
            <p class="mc-totals__value">
              {%- if mc_saved > 0 -%}
                <s class="mc-totals__was"><span class="visually-hidden">Was </span>{{ mc_was_total | money }}</s>
              {%- endif -%}
              <span class="mc-totals__now">{{ cart.total_price | money }}</span>
              {%- if mc_saved > 0 -%}
                <span class="mc-totals__save">
                  <svg viewBox="0 0 12 10" aria-hidden="true"><path fill="currentColor" d="M0 5.2 1.6 3.8 4.6 6.4 10.6.2 12 1.6 4.6 9.2z"/></svg>
                  Save {{ mc_saved | money }}
                </span>
              {%- endif -%}
            </p>
          </div>

          """

CHECKOUT = """            {{ 'sections.cart.checkout' | t }}
"""
CHECKOUT_NEW = """            Checkout · {{ cart.total_price | money_without_trailing_zeros }}
"""

PAY_FOOTER = """            alt="payment"
          >
        </div>
      </div>
    </div>
  </div>
</cart-drawer>"""
PAY_FOOTER_NEW = """            alt="payment"
          >
          <ul class="mc-cart-trust">
            <li><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6 10V8a6 6 0 1 1 12 0v2h1a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V11a1 1 0 0 1 1-1zm2 0h8V8a4 4 0 1 0-8 0z"/></svg>Secure checkout</li>
            <li><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 4h3v16H7zm7 0h3v16h-3z"/></svg>Cancel anytime</li>
            <li><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5zm-1.2 13.6L7.4 12.2l1.4-1.4 2 2 4.4-4.4 1.4 1.4z"/></svg>90-day guarantee</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</cart-drawer>"""


def sub(s, old, new, count=1):
    assert s.count(old) == count, (old[:80], s.count(old))
    return s.replace(old, new)


def cut(s, start, end):
    """Remove from `start` up to (not including) `end`, once."""
    i = s.index(start)
    j = s.index(end, i)
    return s[:i] + s[j:]


def main(src, dst):
    s = open(src).read()
    # Reviews box, empty state and header
    s = cut(s, '<div class="cart-header-top-info">', '<div class="cart-drawer__warnings')
    s = cut(s, '<div class="cart-header-top-info">', "{%- render 'free-shipping-bar' -%}")
    s = sub(s, "        {%- render 'free-shipping-bar' -%}\n", SUB_NOTE)
    s = sub(s, LOOP_OPEN, LOOP_OPEN_NEW)
    s = sub(s, LOOP_CLOSE, LOOP_CLOSE_NEW)
    s = sub(s, NAME, NAME_NEW)
    # The line's price under the title repeats the one on the right; drop it
    s = cut(s, "{%- if item.original_price != item.final_price and is_giveaway_product == false -%}",
            "{%- if item.product.has_only_default_variant == false")
    s = sub(s, CHECKOUT, CHECKOUT_NEW)
    s = sub(s, "                </table>\n", GIFTS)
    s = cut(s, '<div class="totals" role="status">', '<small class="tax-note')
    s = sub(s, '<small class="tax-note', TOTALS_NEW + '<small class="tax-note')
    # Quantities posted with checkout are keyed by line, so the new row order can't shift them
    s = sub(s, 'name="updates[]"', 'name="updates[{{ item.key }}]"')
    s = sub(s, PAY_FOOTER, PAY_FOOTER_NEW)
    s = sub(s, "<style>\n  .drawer {", STYLE.strip() + "\n\n<style>\n  .drawer {")
    open(dst, "w").write(s)
    print("wrote", dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
