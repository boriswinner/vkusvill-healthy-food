<template>
  <div class="container">
    <section class="section home">
      <h1 class="home__header"> Пищевая ценность продуктов из Вкусвилл </h1>
      <p class="home__paragraph">На этом сайте вы можете отсортировать продукты из Вкусвилл по пищевой ценности, содержанию белков, жиров и углеводов. Найдите продукты, подходящие вам - низкокалорийные, низкоуглеводные, высокобелковые и т.п.!</p>
      <p class="home__paragraph">База обновлена: 02.01.2024, для г. Петербург</p>
    </section>

    <section class="section table">
      <TabView :scrollable="true">
        <TabPanel v-for="panel in panels" v-bind:key="panel.name" :header="panel.name">
          <DataTable :value="panel.json" stripedRows paginator :rows="20" sortField="calories" :sortOrder="1" :rowsPerPageOptions="[5, 10, 20, 50, 100, 1000]" tableStyle="min-width: 50rem">
            <Column field="name" sortable header="Название"></Column>
            <Column field="proteins" sortable header="Белки"></Column>
            <Column field="fats" sortable header="Жиры"></Column>
            <Column field="carbs" sortable header="Углеводы"></Column>
            <Column field="calories" sortable header="Ккал"></Column>
            <Column field="price" sortable header="Цена"></Column>
            <Column field="href" header="Ссылка">
              <template #body="slotProps">
                <a target="_blank" rel="noopener noreferrer" :href="slotProps.data.href">Открыть</a>
              </template>              
            </Column>
          </DataTable>          
        </TabPanel>
      </TabView>      

    </section>
  </div>
</template>

<script setup>
useHead({
  titleTemplate: `Вкусвилл: пищевая ценность`,
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
  charset: "utf-8",
  meta: [{ name: "description", content: "Узнайте пищевую ценность продуктов и готовой еды из Вкусвилл. Найдите низкокалорийные, низкоуглеводные продукты." }],
  bodyAttrs: {
    class: "test",
  },
});
</script>

<script>
import gotovaya_eda from './json/gotovaya-eda.json'
import sladosti_i_deserty from './json/sladosti-i-deserty.json'
import zamorozhennye_produkty from './json/zamorozhennye-produkty.json'
import myaso_ptitsa from './json/myaso-ptitsa.json'
import orekhi_chipsy_i_sneki from './json/orekhi-chipsy-i-sneki.json'
import molochnye_produkty_yaytso from './json/molochnye-produkty-yaytso.json'
import khleb_i_vypechka from './json/khleb-i-vypechka.json'
import kolbasy_i_myasnye_delikatesy from './json/kolbasy-i-myasnye-delikatesy.json'
import ovoshchi_frukty_yagody_zelen from './json/ovoshchi-frukty-yagody-zelen.json'
import vegetarianskoe_i_postnoe from './json/vegetarianskoe-i-postnoe.json'
import syry from './json/syry.json'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';                   // optional
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';

export default {
  name: "MyComponent",
  data() {
    return {
      products: [
        {
          name: "name.text",
          proteins: "proteins",
          fats: "fats",
          carbs: "carbs",
          calories: "calories",
          href: "href"
        }
      ],
      panels: [
        {
          name: "Готовая еда",
          json: gotovaya_eda
        },
        {
          name: "Сладости",
          json: sladosti_i_deserty
        },    
        {
          name: "Вегетарианское и постное",
          json: vegetarianskoe_i_postnoe
        },           
        {
          name: "Замороженные продукты",
          json: zamorozhennye_produkty
        },          
        {
          name: "Мясо и птица",
          json: myaso_ptitsa
        },   
        {
          name: "Орехи, чипсы и снэки",
          json: orekhi_chipsy_i_sneki
        },       
        {
          name: "Молочные продукты и яйцо",
          json: molochnye_produkty_yaytso
        },           
        {
          name: "Хлеб и выпечка",
          json: khleb_i_vypechka
        },     
        {
          name: "Колбасы и мясные деликатесы",
          json: kolbasy_i_myasnye_delikatesy
        },               
        {
          name: "Овощи, фрукты, ягоды, зелень",
          json: ovoshchi_frukty_yagody_zelen
        },     
        {
          name: "Сыры",
          json: syry
        },                                             
      ]
    };
  }
}
</script>



<style lang="scss">
// html,body, #__nuxt, #__layout{
  // height:100%!important;
// }

body {
  margin: 0 !important;
}

.container {
	height: 100%;
  min-height: 100%;
	display: flex;
	flex-direction: column;
}



.home {
  background-color:#222222;
  padding: 1em;

  &__header {
    font-family: 'Open Sans Condensed', sans-serif;
    font-size: 48px;
    color: white;
    font-weight: 300;
    margin-bottom: 40px;
  }

  &__paragraph {
    font-family: 'Open Sans', sans-serif;
    font-weight: 400;
    color: #f2f2f2;
    text-align: justify;
    max-width: 70%;
    @media only screen and (min-width: 0px) and (max-width: 660px) {
      max-width: 100%;
    }    
  }
}
</style>
