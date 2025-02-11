import pygame
from controller import Controller

def main():
    pygame.init()
    controller = Controller()

    try:
        while True:
            #controller.update()
            button_status = controller.get_button_status()
            print(button_status)
            pygame.time.delay(500)  # Delay to avoid overwhelming the output
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()