config.load_autoconfig(False)

# config.set("content.user_stylesheets", ["~/.config/qutebrowser/userstyles/tokyonight-storm.css"])
c.url.start_pages = ['https://google.com/']
config.set("colors.webpage.darkmode.enabled", True)

c.url.searchengines = {
    'DEFAULT':  'https://google.com/search?hl=en&q={}',
    '!amazon':       'https://www.amazon.com/s?k={}',
    '!gh':      'https://github.com/search?o=desc&q={}&s=stars',
    '!gimg':      'https://www.google.com/search?tbm=isch&q={}&tbs=imgo:1',
    '!map':       'https://www.google.com/maps/search/{}',
    '!wiki':       'https://en.wikipedia.org/wiki/{}',
    '!yt':      'https://www.youtube.com/results?search_query={}'
}

# === TokyoNight Colors ===
bg = "#313151"
fg = "#c0caf5"
blue = "#7aa2f7"
green = "#9ece6a"
magenta = "#bb9af7"
yellow = "#e0af68"
red = "#f7768e"
cyan = "#7dcfff"
grey = "#565f89"
black = "#212141"
focused = "#515171"

# === Statusbar ===
c.colors.statusbar.normal.bg = bg
c.colors.statusbar.normal.fg = fg
c.colors.statusbar.insert.bg = focused
c.colors.statusbar.insert.fg = blue
c.colors.statusbar.command.bg = focused
c.colors.statusbar.command.fg = blue
c.colors.statusbar.caret.bg = focused
c.colors.statusbar.caret.fg = red
c.colors.statusbar.passthrough.bg = focused
c.colors.statusbar.passthrough.fg = blue
c.colors.statusbar.private.bg = focused
c.colors.statusbar.private.fg = magenta
c.colors.statusbar.progress.bg = focused
c.colors.statusbar.url.fg = focused
c.colors.statusbar.url.error.fg = focused
c.colors.statusbar.url.success.http.fg = focused
c.colors.statusbar.url.success.https.fg = focused
c.colors.statusbar.url.warn.fg = focused

# === Tabs ===
c.colors.tabs.bar.bg = black
c.colors.tabs.indicator.start = blue
c.colors.tabs.indicator.stop = green
c.colors.tabs.indicator.error = red

c.colors.tabs.selected.even.fg = black
c.colors.tabs.selected.even.bg = yellow 
c.colors.tabs.selected.odd.fg = black
c.colors.tabs.selected.odd.bg = yellow 

c.colors.tabs.even.bg = bg
c.colors.tabs.even.fg = grey
c.colors.tabs.odd.bg = bg
c.colors.tabs.odd.fg = grey

c.colors.tabs.pinned.even.bg = magenta
c.colors.tabs.pinned.even.fg = bg
c.colors.tabs.pinned.odd.bg = magenta
c.colors.tabs.pinned.odd.fg = bg
c.colors.tabs.pinned.selected.even.bg = cyan
c.colors.tabs.pinned.selected.even.fg = bg
c.colors.tabs.pinned.selected.odd.bg = cyan
c.colors.tabs.pinned.selected.odd.fg = bg

c.tabs.max_width = 200
c.tabs.padding = {"bottom":20, "left":5, "right":5, "top":20}
c.tabs.position = "left"

c.tabs.show = "always"
c.tabs.indicator.width = 0
c.tabs.favicons.scale = 1.5
c.tabs.title.format = " | {current_title}"

# === Fonts ===
c.fonts.default_family = "Misc Tamsyn"
c.fonts.completion.category = "bold 15pt default_family"
c.fonts.completion.entry = "15pt default_family"
c.fonts.debug_console = "15pt default_family"
c.fonts.downloads = "15pt default_family"
c.fonts.hints = "bold 15pt default_family"
c.fonts.keyhint = "15pt default_family"
c.fonts.messages.error = "15pt default_family"
c.fonts.messages.info = "15pt default_family"
c.fonts.messages.warning = "15pt default_family"
c.fonts.prompts = "15pt default_family"
c.fonts.statusbar = "15pt default_family"


# === Hint Styling (including fonts, borders, and effects) ===

# Hint label background and text color
c.colors.hints.bg = blue
c.colors.hints.fg = bg
c.colors.hints.match.fg = "#f7768e" # matched characters (red)

# Hint popup border (adds a nice border around hint labels)
c.hints.border = "1px solid #7aa2f7" # soft blue border to match theme

# Hint font size and family (match your Neovim font style)
font = "bold 15pt Monospace"  # Monospace for consistency, bold for clarity
c.hints.padding = {"top": 2, "bottom": 2, "left": 4, "right": 4}  # Padding for hints

# Hint opacity & effect
c.hints.radius = 4  # Rounded corners for a smoother look

# === Completion (auto suggestions) ===
c.colors.completion.fg = fg
c.colors.completion.odd.bg = bg
c.colors.completion.even.bg = black
c.colors.completion.category.bg = black
c.colors.completion.category.fg = blue
c.colors.completion.category.border.top = bg
c.colors.completion.category.border.bottom = bg
c.colors.completion.item.selected.bg = blue
c.colors.completion.item.selected.fg = bg
c.colors.completion.item.selected.border.top = blue
c.colors.completion.item.selected.border.bottom = blue
c.colors.completion.match.fg = yellow
c.colors.completion.scrollbar.bg = black
c.colors.completion.scrollbar.fg = fg

# === Downloads ===
c.colors.downloads.bar.bg = bg
c.colors.downloads.start.bg = blue
c.colors.downloads.start.fg = bg
c.colors.downloads.stop.bg = green
c.colors.downloads.stop.fg = bg
c.colors.downloads.error.bg = red
c.colors.downloads.error.fg = bg

# === Prompts (input popups) ===
c.colors.prompts.bg = black
c.colors.prompts.fg = fg
c.colors.prompts.border = f"1px solid {blue}"

# === Messages (errors, warnings, info boxes) ===
c.colors.messages.error.bg = red
c.colors.messages.error.fg = bg
c.colors.messages.warning.bg = yellow
c.colors.messages.warning.fg = bg
c.colors.messages.info.bg = blue
c.colors.messages.info.fg = bg

# === Hints (keyboard hints on links) ===
c.colors.hints.bg = yellow
c.colors.hints.fg = bg
c.colors.hints.match.fg = red

# === Keyhint widget (when you type keys like `f`, `;`, etc.) ===
c.colors.keyhint.bg = bg
c.colors.keyhint.fg = fg
c.colors.keyhint.suffix.fg = yellow

# === Webpage Background ===
c.colors.webpage.bg = bg

# keybindings
config.bind('<space>ff', 'fake-key -g :open<space> ')
config.bind('<space><space>', 'fake-key -g :tab-select<space> ')

# Optional Vim-like navigation
config.bind('gt', 'tab-next')
config.bind('gT', 'tab-prev')

# Optional: Jump directly to tab 1–9
for i in range(1, 10):
    config.bind(f'<space>{i}', f'tab-focus {i-1}')

# statusbar is hidden when nothing happens
c.statusbar.show = "in-mode"
