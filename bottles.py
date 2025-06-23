class Bottles:
    @classmethod
    def song(self) -> str:
        return self.verses(99, 0)

    @classmethod
    def verses(self, starting: int, ending: int) -> str:
        return "\n".join(self.verse(i) for i in range(starting, ending - 1, -1))

    @classmethod
    def verse(self, number: int):
        if number == 0:
            return (
                "No more bottles of beer on the wall, "
                "no more bottles of beer.\n"
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall.\n"
            )
        elif number == 1:
            return (
                "1 bottle of beer on the wall, "
                "1 bottle of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n"
            )
        elif number == 2:
            return (
                "2 bottles of beer on the wall, "
                "2 bottles of beer.\n"
                "Take one down and pass it around, "
                "1 bottle of beer on the wall.\n"
            )
        else:
            return (
                f"{number} bottles of beer on the wall, "
                f"{number} bottles of beer.\n"
                "Take one down and pass it around, "
                f"{number - 1} bottles of beer on the wall.\n"
            )
