import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from repo import *

driver = webdriver.Chrome(executable_path=exe_path)
driver.maximize_window()

driver.get(url)
wait = WebDriverWait(driver, 60)

# Login Steps
wait.until(EC.visibility_of_element_located((By.XPATH, xpsubmit)))
driver.find_element(By.XPATH, xpun).send_keys(user_name)
driver.find_element(By.XPATH, xppsw).send_keys(psw)
driver.find_element(By.XPATH, xpprj).send_keys(project_name)
driver.find_element(By.XPATH, xpsubmit).click()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_parent)))
wait.until(EC.visibility_of_element_located((By.XPATH, xp_home)))

# click on bento menu and selecting contract management
driver.find_element(By.XPATH, xp_bento).click()
driver.switch_to.default_content()
wait.until(EC.visibility_of_element_located((By.XPATH, xp_bento_box)))
driver.find_element(By.XPATH, xp_contract_manage).click()

# SwitchFrame
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_parent))
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_maincontent))
wait.until(EC.visibility_of_element_located((By.XPATH, xp_contracts)))
driver.switch_to.parent_frame()

# Click on contract dropdown and setup contract
driver.find_element(By.XPATH, xp_contracts_dd).click()
driver.switch_to.default_content()
wait.until(EC.visibility_of_element_located((By.XPATH, xp_setup_contract)))
driver.find_element(By.XPATH, xp_setup_contract).click()

# SwitchFrame
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_parent)))
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_maincontent))

# Click on fields tab then click edit create approval button
wait.until(EC.visibility_of_element_located((By.XPATH, xp_fields)))
driver.find_element(By.XPATH, xp_fields).click()
wait.until(
    EC.visibility_of_element_located((By.XPATH, xp_edit_create_approval)))
driver.find_element(By.XPATH, xp_edit_create_approval).click()

# SwitchFrame
driver.switch_to.default_content()
wait.until(EC.visibility_of_element_located((By.XPATH, xp_dialog_box)))
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_create_edit)))

# Verified the count of items for before and after adding the wait-option and also verified the msg of added item.
item_b4_add_wait = driver.find_elements(By.XPATH, xp_execute_action_list)
print("Items in Execute Action List before adding wait option are " + str(len(item_b4_add_wait)))
wait_completion_msg_b4_add_wait = driver.find_elements(By.XPATH, xp_wait_msg_ele)
print("Number of elements with Wait for completion in action List before adding wait option are " + str(
    len(wait_completion_msg_b4_add_wait)))
driver.find_element(By.XPATH, xp_add_wait).click()
wait.until(EC.visibility_of_element_located((By.XPATH, xp_finish)))
wait.until(
    EC.visibility_of_element_located((By.XPATH, xp_execute_action_list)))
item_after_add_wait = driver.find_elements(By.XPATH, xp_execute_action_list)
print("Items in Execute Action List After adding wait option are " + str(len(item_after_add_wait)))
assert len(item_b4_add_wait) < len(item_after_add_wait)
wait_completion_msg_after_add_wait = driver.find_elements(By.XPATH, xp_wait_msg_ele)
print("Number of elements with Wait for completion in action List After adding wait option are " + str(
    len(wait_completion_msg_after_add_wait)))
assert len(wait_completion_msg_b4_add_wait) < len(wait_completion_msg_after_add_wait)
assert wait.until(EC.visibility_of_element_located((By.XPATH, xp_wait_msg_ele)))
print(
    "Assertion For Comparing the count of items Before and After "
    "Clicking the Wait option is done with the above count comparison")
driver.find_element(By.XPATH, xp_finish).click()

# SwitchFrame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_parent))
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_maincontent))
wait.until(EC.visibility_of_element_located((By.XPATH, xp_finish)))
time.sleep(5)

# Click create approval button again
wait.until(
    EC.visibility_of_element_located((By.XPATH, xp_edit_create_approval)))
driver.find_element(By.XPATH, xp_edit_create_approval).click()

# SwitchFrame
driver.switch_to.default_content()
wait.until(EC.visibility_of_element_located((By.XPATH, xp_dialog_box)))
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_create_edit)))

# verify the added item is present or not - For this we are just
# comparing the count of items added last time with now
wait.until(
    EC.visibility_of_element_located((By.XPATH, xp_execute_action_list)))
item_in_list_revisit = driver.find_elements(By.XPATH, xp_execute_action_list)
print("Items in Execute Action List After revisiting the page " + str(len(item_in_list_revisit)))
total_action_element = len(item_after_add_wait)
assert len(item_in_list_revisit) == len(item_after_add_wait)
print("Assertion For count of items For Revisit is done with comparing the count with the previous : " + str(
    len(item_in_list_revisit)))

# This to just scroll till wait button
action = ActionChains(driver)
element = driver.find_element(By.XPATH, xp_add_wait)
action.move_to_element(element).perform()

# TC2--> As discussed here I am continuing to TC1 For TC2 --> continuation To TestCase1-Drag the added wait to 2nd
# position(in between 1st and 2nd item) and click finish
ele_xpath1 = "//div[contains(text(),'Create Approval Actions')]/../../../tr[" + str(total_action_element) + "]/td"
ele_xpath2 = "//div[contains(text(),'Create Approval Actions')]/../../../tr[2]/td"
ele1 = driver.find_element(By.XPATH, ele_xpath1)
ele2 = driver.find_element(By.XPATH, ele_xpath2)
action.drag_and_drop(ele1, ele2).perform()
driver.find_element(By.XPATH, xp_finish).click()

# SwitchFrame
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_parent))
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_maincontent))
wait.until(EC.visibility_of_element_located((By.XPATH, xp_finish)))
time.sleep(5)

# Click create approval button again
wait.until(
    EC.visibility_of_element_located((By.XPATH, xp_edit_create_approval)))
driver.find_element(By.XPATH, xp_edit_create_approval).click()

driver.switch_to.default_content()
wait.until(EC.visibility_of_element_located((By.XPATH, xp_dialog_box)))
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_create_edit)))
wait.until(
    EC.visibility_of_element_located((By.XPATH, xp_execute_action_list)))

# By verifying the Wait msg is at 2nd position using xpath
# we are verifying dropped element's position is at 2nd number
msg = driver.find_element(By.XPATH, xp_for_item_at_2nd_position).text
assert msg == msg_expected
print("Assertion For Msg Of Added Wait item is done and actual msg is " + str(msg))
driver.find_element(By.XPATH, xp_finish).click()

# SwitchFrame
driver.switch_to.default_content()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_parent)))

# Click on Contract on Top Navigation --> Clk New --> Select Contract Type -->Fill Title and Disc
driver.find_element(By.XPATH, xp_contract_top_nav).click()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_maincontent)))
wait.until(EC.visibility_of_element_located((By.XPATH, xp_new)))
driver.find_element(By.XPATH, xp_new).click()
action = ActionChains(driver)
wait.until(EC.visibility_of_element_located((By.XPATH, xp_contract_type)))
element_contract_type = driver.find_element(By.XPATH, xp_contract_type)
sel = Select(element_contract_type)
sel.select_by_visible_text("Master Services Agreement")
driver.find_element(By.XPATH, xp_contract_title).send_keys("Test")
driver.find_element(By.XPATH, xp_contract_disc).send_keys("Agiloft Automation Test")
driver.find_element(By.XPATH, xp_save_dd).click()

# SwitchFrame
driver.switch_to.default_content()

# Clk save and continue
wait.until(EC.visibility_of_element_located((By.XPATH, xp_save_continue)))
driver.find_element(By.XPATH, xp_save_continue).click()

# SwitchFrame
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_parent)))
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_maincontent))

# Click on Approval and verified Number of approval needed are zero
# We know if table has entry then header will be their and vice versa
# So based on the style of header which is hidden or not Verified Table has No records
wait.until(EC.visibility_of_element_located((By.XPATH, xp_approval)))
ele_approval = driver.find_element(By.XPATH, xp_approval)
driver.execute_script("arguments[0].click();", ele_approval)
wait.until(EC.visibility_of_element_located((By.XPATH, xp_number_of_approval_nneded)))
approval_needed = driver.find_element(By.XPATH, xp_number_of_approval_nneded).text
assert approval_needed == str(0)
print("Assertion For Number of approval needed Before Create approval is done and count is " + str(approval_needed))
style_attributes = driver.find_element(By.XPATH, xp_table_header).get_attribute("style")
assert "display: none" in style_attributes
print(
    "Assertion For No Entry in table is done with Header of "
    "table is not displayed and hence verified no entry is present")
driver.find_element(By.XPATH, xp_create_approval).click()
wait.until(EC.visibility_of_element_located((By.XPATH, xp_launch_approval)))
style_attributes_after_approval = driver.find_element(By.XPATH, xp_table_header).get_attribute("style")
assert "display: none" not in style_attributes_after_approval
print(
    "Assertion For Checking the entry in table After Create approval "
    "by checking the table has header Now as it has new entry")
approval_needed_after_approval = driver.find_element(By.XPATH, xp_number_of_approval_nneded).text
assert approval_needed_after_approval == str(1)
print("Assertion For Number of approval needed After Create approval is done and count is " + str(
    approval_needed_after_approval))

# SwitchFrame
driver.switch_to.default_content()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xp_frame_parent)))
driver.switch_to.frame(driver.find_element(By.XPATH, xp_frame_top_info))
driver.find_element(By.XPATH, xp_clk_profile).click()
driver.switch_to.default_content()

# Logout
driver.find_element(By.XPATH, xp_clk_logout).click()
print("Logout Successfully")
wait.until(EC.visibility_of_element_located((By.XPATH, xpsubmit)))
driver.close()
