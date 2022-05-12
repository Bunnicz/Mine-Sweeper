import settings


def height_prct(percentage: int) -> int:
    return (settings.HEIGHT / 100) * percentage


def width_prct(percentage: int) -> int:
    return (settings.WIDTH / 100) * percentage


if __name__ == "__main__":
    print(height_prct(25))
    print(width_prct(25))
