# Album
Note: If *jsonplaceholder* links are not available, please, use any VPN in our traffic.

In this laboratory work you have to try to use the *Route and Http* modules in your Angular project.

1. URL: /home - static markup page
2. URL: /about - static markup page
3. You should have CRUD (create / read / update / delete) operations for albums.
4. URL: /albums - a list of albums from this url. Each item should:
    * have delete button with implementation
    * be clickable, after selecting one of them, a detail page must be opened.
5. URL: /albums/:id - detail page of selected item (example). This page should contain:
    * information about selected item
    * editable input for changing album title and “Save” button
    * “Return back” button
    * “Photos” link which will redirect to photos page of selected album
6. URL: /albums/:id/photos - photos page of selected album (example). This page will render all images in any format and will have a “Return back” button.
7. Root url: “”, must be redirect to: /home 
8. Albums and photos must be fetched using HTTP module and must be passed to components through albums.service.ts and must be Observable
9. Your components:
    * Home Component
    * About Component
    * Albums Component
    * Album Detail Component
    * Album Photos Component

Useful links
- <a href="https://angular.io/guide/router" target="_blank">Router Module</a>
- <a href="https://angular.io/guide/observables" target="_blank">Observables</a>
- <a href="https://angular.io/guide/http" target="_blank">Http Client Module</a>
- <a href="https://angular.io/tutorial/toh-pt4" target="_blank">Angular Services</a>

GOOD LUCK :)

