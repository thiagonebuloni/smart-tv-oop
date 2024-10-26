from enum import Enum


class Channels(Enum):
    CULTURA = 2
    SBT = 4
    GLOBO = 5
    RECORD = 7
    GAZETA = 11
    BAND = 13
    REDETV = 9
    FUTURA = 15
    TV_ESCOLA = 16
    TV_BRASIL = 17
    TV_CAMARA = 18
    TV_SENADO = 19
    TV_JUSTICA = 20


class SmartTv:
    volume: int = 10
    channel: Channels = Channels.SBT
    on: bool = False

    tv_off_message: str = "\nA TV está desligada."

    def power_on_off(self) -> None:
        self.on = not self.on

        if self.on:
            self.view()
        else:
            print("\033c", end="")
            print(self.tv_off_message)
            input()

    def increase_volume(self) -> None:
        if self.on:
            if self.volume < 20:
                self.volume += 1
            else:
                print("Volume muito alto pode prejudicar seus ouvidos, lindo.")
                input()
            # self.view(volume=self.volume)
            volume_graphic = "█" * self.volume
            volume_on_screen = f"Volume: {self.volume} {volume_graphic}"
            self.view(volume=volume_on_screen)
        else:
            print(self.tv_off_message)

    def decrease_volume(self) -> None:
        if self.on:
            if self.volume == 0:
                self.view("MUDOO!!")
                return
            self.volume -= 1
            volume_graphic = "█" * self.volume
            volume_on_screen = f"Volume: {self.volume} {volume_graphic}"
            self.view(volume=volume_on_screen)
        else:
            print(self.tv_off_message)
            input()
            print("\033c", end="")

    def increase_channel(self) -> None:
        if self.on:
            try:
                if self.channel.value == 19:
                    new_channel = 2
                    self.channel = Channels(new_channel)
                    channel_on_screen = f"Canal: {self.channel.name}"
                    self.view(canal=channel_on_screen)
                    return
                new_channel = self.channel.value + 1
                self.channel = Channels(new_channel)
            except ValueError:
                new_channel = self.channel.value + 2
                self.channel = Channels(new_channel)
        # print(f"Canal: {self.canal.name}")
        channel_on_screen = f"Canal: {self.channel.name}"
        self.view(canal=channel_on_screen)

    def decrease_channel(self) -> None:
        if self.on:
            try:
                if self.channel.value < 3:
                    new_channel = 20
                    self.channel = Channels(new_channel)
                    channel_on_screen = f"Canal: {self.channel.name}"
                    self.view(canal=channel_on_screen)
                    return
                new_channel = self.channel.value - 1
                self.channel = Channels(new_channel)
            except ValueError:
                new_channel = self.channel.value - 2
                self.channel = Channels(new_channel)
        channel_on_screen = f"Canal: {self.channel.name}"
        self.view(canal=channel_on_screen)

    def select_channel(self, canal: Channels) -> None:
        if self.on:
            try:
                self.channel = canal
                channel_on_screen = f"Canal: {self.channel.name}"
                self.view(canal=channel_on_screen)
            except ValueError:
                print("Canal inválido.")
        else:
            print(self.tv_off_message)

    def view(self, volume: str = "", canal: str = ""):
        print("\033c", end="")
        if volume == "":
            volume_space = 31
        else:
            volume_space = 31 - len(volume)

        if canal == "":
            canal_space = 31
        else:
            canal_space = 31 - len(canal)

        bar = "---------------------------------"
        vertical = "|" + " " * 32 + "|"
        vertical_channel = "| " + canal + " " * canal_space + "|"
        vertical_volume = "| " + volume + " " * volume_space + "|"
        foot = """               ||                
          ------------"""

        # Draw TV
        print()
        print(bar)
        print(vertical_channel)  # canal
        for _ in range(4):
            print(vertical)
        print(vertical_volume)  # volume
        print(bar)
        print(foot)

    def menu(self) -> int:
        print()
        print("1 - Ligar/Desligar")
        print("2 - Aumentar volume")
        print("3 - Diminuir volume")
        print("4 - Aumenta de canal")
        print("5 - Diminui de canal")
        print("6 - Escolher canal")
        print("0 - Sair")
        try:
            user_selection = int(input("Escolha uma opção: "))
        except ValueError:
            self.se_tv_ligada()
            print("Opção inválida.")
            input()
            self.se_tv_ligada()
            user_selection = 99
        return user_selection

    def se_tv_ligada(self):
        if tv.on:
            self.view()


user_selection = 99
tv = SmartTv()
print("\033c", end="")
while user_selection > 0:
    user_selection = tv.menu()

    try:
        match user_selection:
            case 1:
                tv.power_on_off()
            case 2:
                tv.increase_volume()
            case 3:
                tv.decrease_volume()
            case 4:
                tv.increase_channel()
            case 5:
                tv.decrease_channel()
            case 6:
                canal = int(input("Escolha um canal: "))
                try:
                    tv.select_channel(Channels(canal))
                except ValueError:
                    tv.se_tv_ligada()
                    print("\nCanal inválido.")
                    input()
                    print("\033c", end="")

            case 0:
                tv.power_on_off()
            case default:
                tv.se_tv_ligada()
                print("\nOpção inválida.")
                input()
                print("\033c", end="")

    except ValueError:
        print("\nOpção inválida.")
        input()
        print("\033c", end="")
