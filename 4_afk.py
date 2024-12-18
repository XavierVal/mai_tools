import pyautogui
import time
import random
import argparse
import logging

def move_mouse_randomly(interval=30, percentage=30):
    """
    Mueve el ratón aleatoriamente en la pantalla.
    :param interval: cada X segundos se moverá el ratón
    :param percentage: porcentaje de movimiento en relación al tamaño de la pantalla
    :return:
    """
    start_time = time.time()
    try:
        while True:
            my_x, my_y = pyautogui.position()
            move_x = round(random.randint(-pyautogui.size().width, pyautogui.size().width) / percentage)
            move_y = round(random.randint(-pyautogui.size().height, pyautogui.size().height) / percentage)

            x = my_x - move_x
            y = my_y - move_y
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(interval)
            elapsed_time = time.time() - start_time
            logging.info(f"Moving to: {move_x},{move_y} -> [{x}, {y}]")
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        logging.info(f" --- The end. --- | Tiempo de uso: {elapsed_time:.2f} segundos")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mueve el ratón aleatoriamente en la pantalla.")
    parser.add_argument("-i", "--interval", type=float, default=30, help="Intervalo de tiempo en segundos (por defecto 30s)")
    parser.add_argument("-p", "--percentage", type=float, default=30, help="Porcentaje de movimiento (por defecto 30%)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        move_mouse_randomly(args.interval, args.percentage)
    except ValueError:
        logging.error("Entrada inválida, introduce un número válido.")
    except Exception as e:
        logging.error(f"Error: {e}")