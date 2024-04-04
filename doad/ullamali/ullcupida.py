# Wait for an element to be visible
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "my-element")))

# Wait for an element to be clickable
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "my-element")))

# Wait for a page to load
WebDriverWait(driver, 10).until(EC.title_is("My Page Title"))
