import time
from playwright.sync_api import sync_playwright, expect
import re

def test_login_camino_feliz():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False,slow_mo=300)
        url = "https://auth.uber.com/v2/?breeze_init_req_id=fd19ea6a-248d-46b3-ac46-b03f407c3d28&breeze_local_zone=dca23&next_url=https%3A%2F%2Fm.uber.com%2Flogin-redirect%2F%3Fmarketing_vistor_id%3De2976ac3-acc3-4918-980c-42a52132fc03%26uclick_id%3Daef86359-4d49-4588-b45b-81bd2d87d5dd&sm_flow_id=19n5F82b&state=pjgEdtPDORMiAAJBSXShALrMMJwpwLAItljk7sbJQsA%3D"
        page = browser.new_page()
        
        page.goto(url)
        
        page.fill("input[name='email']", "a123@uade.edu.ar")
        page.click("button[id='forward-button']")

       
        mensaje_error = page.get_by_text(re.compile(r"Correo electrónico ingresado no válido\."))

        expect(mensaje_error).not_to_be_visible(timeout=3000)
        
        
        print("Camino Feliz exitoso: El mensaje de error no apareció.")

        

if __name__ == "__main__":
    test_login_camino_feliz()