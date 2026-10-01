import pyfiglet


def main():
    print("=== ASCII Art Generator ===")

    # Get all fonts available in PyFiglet
    fonts = pyfiglet.FigletFont.getFonts()

    font = input("Enter type of font [slant]: ").strip() or "slant"
    text = input("Enter your text [Text]: ").strip() or "Text"

    if font in fonts:
        result = pyfiglet.figlet_format(
            text,
            font=font
        )
        print("\n" + result)

    else:
        print(f"\nSorry, '{font}' font was not found.")
        print("Error 404: Font not available.")

        print("\nAvailable fonts:")
        print(", ".join(fonts))


if __name__ == "__main__":
    main()
