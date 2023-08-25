import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.HashMap;
import java.util.Map;

public class PageUtilities {
    private int timeout = 5;
    private WebDriver driver;
    private boolean useCoordinates = false;
    private boolean takeScreenshotBeforeClick = false;
    private Map<String, Integer> screenshotCount = new HashMap<>();

    public PageUtilities(WebDriver driver) {
        this.driver = driver;
    }

    public boolean isUseCoordinates() {
        return useCoordinates;
    }

    public void setUseCoordinates(boolean useCoordinates) {
        this.useCoordinates = useCoordinates;
    }

    public boolean isTakeScreenshotBeforeClick() {
        return takeScreenshotBeforeClick;
    }

    public void setTakeScreenshotBeforeClick(boolean takeScreenshotBeforeClick) {
        this.takeScreenshotBeforeClick = takeScreenshotBeforeClick;
    }

    public void takeScreenshot() {
        String currentUrl = driver.getCurrentUrl();
        screenshotCount.putIfAbsent(currentUrl, 0);
        int count = screenshotCount.get(currentUrl) + 1;
        screenshotCount.put(currentUrl, count);

        String filename = currentUrl.replace("/", "_") + "_" + count + ".png";
        String filepath = "screenshots/" + filename;

        // Assuming you have a method to capture screenshots in your WebDriver
        // implementation
        // driver.takeScreenshot(filepath);
    }

    public WebElement clickElement(By elementLocator) {
        if (useCoordinates) {
            return clickElementCoordinates(elementLocator);
        } else {
            try {
                WebDriverWait wait = new WebDriverWait(driver, timeout);
                WebElement clickElem = wait.until(ExpectedConditions.elementToBeClickable(elementLocator));
                clickElem.click();
                return clickElem;
            } catch (Exception e) {
                System.out.println("\nTimed out looking for " + elementLocator + ", will click anyway");
                return null;
            }
        }
    }

    public WebElement clickElementCoordinates(By elementLocator) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeout);
            WebElement coordElem = wait.until(ExpectedConditions.elementToBeClickable(elementLocator));

            int elementX = coordElem.getLocation().getX() + coordElem.getSize().getWidth() / 2;
            int elementY = coordElem.getLocation().getY() + coordElem.getSize().getHeight() / 2;

            Actions action = new Actions(driver);
            action.moveToElement(coordElem, elementX, elementY).click().perform();

            return coordElem;
        } catch (Exception e) {
            System.out.println("\nTimed out looking for " + elementLocator + ", will click anyway");
            return null;
        }
    }

    public WebElement setAttributeValue(By elementLocator, String keys) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeout);
            WebElement elem = wait.until(ExpectedConditions.elementToBeClickable(elementLocator));
            elem.clear();
            elem.sendKeys(keys);
            return elem;
        } catch (Exception e) {
            // Handle exception if needed
            return null;
        }
    }

    public WebElement sendKeystrokesToElement(By elementLocator, String keys) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeout);
            WebElement elem = wait.until(ExpectedConditions.elementToBeClickable(elementLocator));
            elem.clear();

            Actions action = new Actions(driver);
            for (char key : keys.toCharArray()) {
                action.keyDown(Character.toString(key)).keyUp(Character.toString(key));
            }
            action.perform();

            return elem;
        } catch (Exception e) {
            // Handle exception if needed
            return null;
        }
    }

    public String getAttributeValue(By elementLocator, String attribute) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeout);
            WebElement elem = wait.until(ExpectedConditions.elementToBeClickable(elementLocator));
            return elem.getAttribute(attribute);
        } catch (Exception e) {
            // Handle exception if needed
            return null;
        }
    }

    public String elementText(By elementLocator) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeout);
            WebElement elem = wait.until(ExpectedConditions.elementToBeClickable(elementLocator));
            return elem.getText();
        } catch (Exception e) {
            // Handle exception if needed
            return null;
        }
    }

    public boolean elementIsDisplayed(By elementLocator, int timeout) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeout);
            return wait.until(ExpectedConditions.visibilityOfElementLocated(elementLocator)).isDisplayed();
        } catch (Exception e) {
            // Handle exception if needed
            return false;
        }
    }

    public WebElement awaitClickable(By elementLocator) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeout);
            return wait.until(ExpectedConditions.elementToBeClickable(elementLocator));
        } catch (Exception e) {
            // Handle exception if needed
            return null;
        }
    }

    public String handleAlertWindow(WebDriver driver) {
        try {
            Alert alert = driver.switchTo().alert();
            String resultText = alert.getText();
            alert.accept();
            return resultText;
        } catch (Exception e) {
            // Handle exception if needed
            return null;
        }
    }

    public boolean checkHome(WebDriver browser) {
        try {
            String result = browser.getCurrentUrl().toLowerCase();
            if (result.contains("home")) {
                return true;
            } else {
                Thread.sleep(1000);
                result = browser.getCurrentUrl().toLowerCase();
                return result.contains("home");
            }
        } catch (Exception e) {
            // Handle exception if needed
            return false;
        }
    }

    public void scrollPageBottom(WebDriver browser) {
        try {
            ((JavascriptExecutor) browser).executeScript("window.scrollTo(0, document.body.scrollHeight);");
        } catch (Exception e) {
            // Handle exception if needed
        }
    }
}