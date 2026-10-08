(() => {
  const screens = window.TALKI_MOCKUPS;
  const catalogue = document.querySelector('#catalogue');
  const search = document.querySelector('#search');
  const device = document.querySelector('#device');
  const viewer = document.querySelector('#viewer');
  const image = document.querySelector('#viewer-image');
  const stage = document.querySelector('#image-stage');
  const params = new URLSearchParams(location.search);
  const categoryNames = {all: 'Todas las pantallas', landing: 'Landing pública', app: 'Pantallas de la aplicación', states: 'Estados de interacción'};
  let category = ['landing', 'app', 'states'].includes(params.get('categoria')) ? params.get('categoria') : 'all';
  device.value = {web: 'web', movil: 'mobile'}[params.get('vista')] || 'all';
  search.value = params.get('buscar') || '';
  let visibleImages = [], current = 0, zoom = null, previousFocus = null;
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const element = (tag, cls, text) => {const node = document.createElement(tag); if(cls) node.className = cls; if(text) node.textContent = text; return node;};
  function syncURL() {
    const url = new URL(location.href);
    const entries = {categoria: category === 'all' ? '' : category, vista: device.value === 'mobile' ? 'movil' : device.value === 'web' ? 'web' : '', buscar: search.value.trim()};
    for (const [key, value] of Object.entries(entries)) value ? url.searchParams.set(key, value) : url.searchParams.delete(key);
    history.replaceState(null, '', url);
  }
  function render() {
    catalogue.replaceChildren(); visibleImages = [];
    const query = normalize(search.value.trim());
    const filtered = screens.filter(screen => (category === 'all' || category === screen.category) && normalize(`${screen.id} ${screen.title} ${screen.description}`).includes(query));
    for (const screen of filtered) {
      const pictures = screen.images.filter(pic => device.value === 'all' || pic.device === device.value);
      if (!pictures.length) continue;
      const card = element('article', 'card'); card.id = screen.id.toLowerCase();
      const top = element('div', 'card-top'); top.append(element('span', 'code', screen.id), element('h3', '', screen.title)); card.append(top);
      const previews = element('div', `previews${pictures.length === 1 ? ' single' : ''}`);
      for (const pic of pictures) {
        const index = visibleImages.length; visibleImages.push({...pic, screen});
        const preview = element('div', `preview ${pic.device}`);
        const button = element('button', 'image-button'); button.type = 'button'; button.setAttribute('aria-label', `Ampliar ${screen.title}, ${pic.device === 'mobile' ? 'móvil' : 'web'}`);
        const thumb = element('img'); thumb.src = pic.src; thumb.alt = pic.alt; thumb.loading = index < 4 ? 'eager' : 'lazy'; thumb.decoding = 'async'; button.append(thumb); button.addEventListener('click', () => open(index));
        const caption = element('div', 'image-caption'); caption.append(element('span', '', pic.device === 'mobile' ? 'MÓVIL' : 'WEB'));
        const link = element('a', '', 'Imagen completa ↗'); link.href = pic.src; link.target = '_blank'; link.rel = 'noopener'; link.setAttribute('aria-label', `Abrir imagen completa de ${screen.title}, ${pic.device === 'mobile' ? 'móvil' : 'web'}`); caption.append(link);
        preview.append(button, caption); previews.append(preview);
      }
      card.append(previews, element('p', 'card-description', screen.description)); catalogue.append(card);
    }
    document.querySelector('#empty').hidden = catalogue.children.length !== 0;
    document.querySelector('#catalogue-title').textContent = categoryNames[category];
    document.querySelector('#result-count').textContent = `${catalogue.children.length} ${catalogue.children.length === 1 ? 'pantalla' : 'pantallas'} · ${visibleImages.length} ${visibleImages.length === 1 ? 'mock-up' : 'mock-ups'}`;
    for (const button of document.querySelectorAll('[data-category]')) button.setAttribute('aria-pressed', String(button.dataset.category === category));
    syncURL();
  }
  function fit() {zoom = null; stage.classList.remove('zoomed'); image.style.width = ''; document.querySelector('#zoom-label').textContent = 'Ajustar'; stage.scrollTop = stage.scrollLeft = 0;}
  function display(index) {
    current = index; const pic = visibleImages[current];
    document.querySelector('#viewer-title').textContent = `${pic.screen.id}: ${pic.screen.title}`;
    document.querySelector('#viewer-device').textContent = pic.device === 'mobile' ? 'MOCK-UP MÓVIL' : 'MOCK-UP WEB';
    image.src = pic.src; image.alt = pic.alt; document.querySelector('#original').href = pic.src;
    document.querySelector('#image-position').textContent = `${current + 1} / ${visibleImages.length}`;
    document.querySelector('#previous').disabled = current === 0;
    document.querySelector('#next').disabled = current === visibleImages.length - 1;
    fit();
  }
  function open(index) {previousFocus = document.activeElement; viewer.showModal(); document.body.style.overflow = 'hidden'; display(index); document.querySelector('#close').focus();}
  function changeZoom(direction) {
    if(!image.naturalWidth) return;
    const currentScale = zoom ?? image.getBoundingClientRect().width / image.naturalWidth;
    zoom = Math.max(.1, Math.min(3, currentScale + direction * .25));
    stage.classList.add('zoomed'); image.style.width = `${Math.round(image.naturalWidth * zoom)}px`;
    document.querySelector('#zoom-label').textContent = `${Math.round(zoom * 100)} %`;
  }
  document.querySelector('#close').addEventListener('click', () => viewer.close());
  viewer.addEventListener('close', () => {document.body.style.overflow = ''; previousFocus?.focus();});
  viewer.addEventListener('click', event => {if(event.target === viewer) {const rect = viewer.getBoundingClientRect(); if(event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) viewer.close();}});
  viewer.addEventListener('keydown', event => {if(event.key === 'ArrowRight' && current < visibleImages.length - 1) {event.preventDefault(); display(current + 1);} if(event.key === 'ArrowLeft' && current > 0) {event.preventDefault(); display(current - 1);}});
  document.querySelector('#next').addEventListener('click', () => display(current + 1));
  document.querySelector('#previous').addEventListener('click', () => display(current - 1));
  document.querySelector('#zoom-in').addEventListener('click', () => changeZoom(1));
  document.querySelector('#zoom-out').addEventListener('click', () => changeZoom(-1));
  document.querySelector('#fit').addEventListener('click', fit);
  for(const button of document.querySelectorAll('[data-category]')) button.addEventListener('click', () => {category = button.dataset.category; render();});
  search.addEventListener('input', render); device.addEventListener('change', render);
  document.querySelector('#reset').addEventListener('click', () => {category = 'all'; device.value = 'all'; search.value = ''; render(); search.focus();});
  render();
  if(location.hash) requestAnimationFrame(() => document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView());
})();
