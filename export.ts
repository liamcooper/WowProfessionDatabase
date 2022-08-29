const {remote} = require('webdriverio');
const fs = require('fs');
const _ = require('lodash');

class Reagent {
    Name: string;
    Quantity: number;
}

class Item {
    Profession: string;
    ID: number;
    Name: string;
    Learn: number;
    Yellow: number;
    Green: number;
    Grey: number;
    Source: string;
    RecipeID: number;
    Reagents: { [name: string]: number };
    Phase: number;
}

;(async () => {
    const browser = await remote({
        capabilities: {
            browserName: 'chrome'
        }
    });

    await browser.setTimeout({ 'pageLoad': 10000 })

    await browser.url("https://www.wowhead.com/wotlk/spells/professions");

    const cookieRejectButton = await browser.$('#onetrust-reject-all-handler');
    if (await cookieRejectButton.isExisting()) {
        await cookieRejectButton.click();
    }

    let rows = [];

    await getRowUrls();
    let button = await getNextButton();
    while (await button.isExisting()) {
        await button.click();
        await getRowUrls();
        button = await getNextButton();
    }

    const items = [];
    for (const row of rows) {
        const item = await parseRow(row);
        if (item) {
            items.push(item);
        }
    }

    const grouped = _.groupBy(items, 'Profession');

    for (const group of Object.keys(grouped)) {
        let groupedItems = grouped[group];
        groupedItems = _.keyBy(groupedItems, 'Name');
        Object.keys(groupedItems).forEach(group => {
            delete groupedItems[group].Name;
            delete groupedItems[group].Profession;
        })
        const rowsText = JSON.stringify(groupedItems);
        await fs.writeFile(`./${ group }.json`, rowsText, 'utf-8', err => {
            if (err) {
                console.error(err);
            }
        });
    }

    await browser.deleteSession();

    async function getRowUrls() {
        const newRows = await browser.$$('//div[@id="lv-spells"]//table/tbody/tr/td[2]//a');
        const rowUrls = await Promise.all(newRows.map(async row => await row.getAttribute('href')));
        rows = [...rows, ...rowUrls];
    }

    async function getNextButton() {
        return browser.$('//div[@id="lv-spells"]/div[contains(@class, "listview-band-top")]//div[contains(@class,"listview-nav")]//a[contains(text(), "Next")][@data-active="yes"]');
    }

    async function parseRow(url) {
        try {
            await browser.url(`${ url }#recipes`);

            const cookieRejectButton = await browser.$('#onetrust-reject-all-handler');
            if (await cookieRejectButton.isExisting()) {
                await cookieRejectButton.click();
            }

            const item = new Item();

            const craftedItemAnchor = await browser.$(`//table[@class="icontab"]//a`);
            if (!await craftedItemAnchor.isExisting()) {
                return;
            }
            item.ID = getNumberFromString(await craftedItemAnchor.getAttribute('href'));

            const professionElement = await browser.$('//div[@class = "breadcrumb"]/span[last()]');
            item.Profession = (await professionElement.getText()).toLowerCase();

            item.Name = await browser.$('h1').getText();
            item.RecipeID = getNumberFromString(url);

            const levelInfoElements = await browser.$$('//table[@class="infobox"]//div[@id="infobox-contents-0"]/ul/li/div[contains(text(), "Difficulty")]/span');
            if (levelInfoElements.length > 0) {
                item.Learn = await levelInfoElements[0].getText();
                try {
                    item.Yellow = await browser.$('//table[@class="infobox"]//div[@id="infobox-contents-0"]/ul/li/div[contains(text(), "Difficulty")]/span[@class="r2"]').getText();                    
                } catch (e) {}
                try {
                    item.Green = await browser.$('//table[@class="infobox"]//div[@id="infobox-contents-0"]/ul/li/div[contains(text(), "Difficulty")]/span[@class="r3"]').getText();
                } catch (e) {}
                try {
                    item.Grey = await browser.$('//table[@class="infobox"]//div[@id="infobox-contents-0"]/ul/li/div[contains(text(), "Difficulty")]/span[@class="r4"]').getText();
                } catch (e) {}
            }
            const tableColumns = await Promise.all((await browser.$$('//div[@class = "listview"]//table/thead/tr/th//a//span//span'))
                .map(async row => await row.getText()));
            const index = tableColumns.indexOf('Source');
            item.Source = await browser.$(`//div[@class = "listview"]//table/tbody/tr/td[${ index + 2 }]`).getText();
            if (!item.Source) {
                item.Source = 'Trainer';
            }
            item.Phase = 1;

            let reagentIdRows = await browser.$$('//table[@id="icon-list-reagents"]/tbody/tr');
            let reagentKeyRows = await browser.$$('//table[@id="icon-list-reagents"]/tbody/tr[not(not(@id))]//a[2]');
            let reagentValueRows = await browser.$$('//table[@id="icon-list-reagents"]/tbody/tr//span[@class = "icon-list-quantity-wrapper"]');
            if (reagentKeyRows.length === 0) {
                reagentIdRows = await browser.$$('//table[@class="icon-list"]/tbody/tr');
                reagentKeyRows = await browser.$$('//table[@class="icon-list"]/tbody/tr/td/a');
                reagentValueRows = await browser.$$('//table[@class="icon-list"]/tbody/tr/td/span[@class = "icon-list-quantity-wrapper"]');
            }

            let reagents = [];
            let x = 0;
            for (const row of reagentKeyRows) {
                const id = await reagentIdRows[x].getAttribute('id');
                if (id?.match(/\.+/g).length > 1) {
                    x++;
                    continue;
                }

                const key = await row.getText();
                const value = Number(await reagentValueRows[x].getAttribute('data-icon-list-quantity'));

                const reagent = new Reagent();
                reagent.Name = key;
                reagent.Quantity = value;
                reagents.push(reagent);

                x++;
            }

            reagents = reagents.filter(m => !!m);

            reagents = _.groupBy(reagents, 'Name');
            item.Reagents = _.mapValues(reagents, m => m[0].Quantity);

            return item;
        } catch (e) {
            console.error(e);
            await parseRow(url);
        }
    }

    function getNumberFromString(string) {
        return Number(new RegExp(/\d+/).exec(string));
    }
})()