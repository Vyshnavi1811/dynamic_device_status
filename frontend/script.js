const companySelect = document.getElementById("cs");
const deviceContainer = document.getElementById("dc");

async function fetchCompanies() {
  const res = await fetch("http://127.0.0.1:5000/companies");
  const companies = await res.json();

  companySelect.innerHTML = companies
    .map(c => `<option value="${c.id}">${c.name}</option>`)
    .join("");

  if (companies.length > 0) {
    fetchDevices(companies[0].id);
  }
}

async function fetchDevices(companyId) {
  const res = await fetch(`http://127.0.0.1:5000/devices/${companyId}`);
  const devices = await res.json();

  deviceContainer.innerHTML = devices.map(d => `
    <div class="device-tile ${d.status}">
      <h3>${d.name}</h3>
      <p>${d.status.toUpperCase()}</p>
    </div>
  `).join("");
}

companySelect.addEventListener("change", (e) => {
  fetchDevices(e.target.value);
});

setInterval(() => {
  const companyId = companySelect.value;
  if (companyId) fetchDevices(companyId);
}, 10000);

fetchCompanies();
