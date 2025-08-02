A Telegram bot that combines two images into one. The bot works with photos sent by the user and automatically creates a collage from the last two received images.

</br>
<div>
    <a href="README.md">
        <img src="https://img.shields.io/badge/README-RU-blue?color=006400&labelColor=006400&style=for-the-badge">
    </a>
    <a href="README.en.md">
        <img src="https://img.shields.io/badge/README-ENG-blue?color=44944a&labelColor=1C2325&style=for-the-badge">
    </a>
</div>
</br>

![obscuraBot](obscuraBot.webp)

## How It Works
1. The user sends two images to the bot one after the other.
2. The bot saves these images.
3. When the second image is received, the bot:
   - Downloads both images from Telegram servers.
   - Creates a new image where both original images are placed horizontally.
   - Sends the result back to the user.
   - Clears the queue of received images.

## Technologies
- Python 3
- `python-telegram-bot`
- `Pillow`
- `requests`

## Possible Applications
**Creating "Before/After" Comparisons**:
   - Demonstrating changes (renovation, transformation)
   - Comparing results of cosmetic procedures

**Creating Collages**:
   - Combining two related images
   - Comparing alternative options

**Educational Purposes**:
   - Comparing historical and modern views of landscapes
   - Demonstrating scientific experiments
   - Showing changes in nature
