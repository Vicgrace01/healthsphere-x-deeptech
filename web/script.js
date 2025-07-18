function simulateVitals() {
  const temp = (36 + Math.random() * 3).toFixed(1);
  const heart = Math.floor(60 + Math.random() * 40);
  const spo2 = Math.floor(94 + Math.random() * 5);
  const systolic = Math.floor(110 + Math.random() * 20);
  const diastolic = Math.floor(70 + Math.random() * 15);
  const bp = `${systolic}/${diastolic}`;

  document.getElementById('temp').textContent = `${temp} °C`;
  document.getElementById('heart').textContent = `${heart} bpm`;
  document.getElementById('spo2').textContent = `${spo2} %`;
  document.getElementById('bp').textContent = `${bp} mmHg`;

  updateRecommendation(temp, heart, spo2, systolic, diastolic);
}

function updateRecommendation(temp, heart, spo2, sys, dia) {
  let recommendation = "Vitals look normal. Keep monitoring.";

  if (temp > 38.5) {
    recommendation = "⚠️ High fever detected. Recommend paracetamol, hydration, and rest.";
  }

  if (spo2 < 92) {
    recommendation = "🆘 Low SpO2! Consider oxygen therapy or call emergency services.";
  }

  if (sys > 140 || dia > 90) {
    recommendation = "⚠️ High blood pressure. Reduce salt, avoid stress, consult doctor.";
  }

  if (heart > 100) {
    recommendation = "⚠️ Elevated heart rate. Ensure rest and hydration.";
  }

  document.getElementById('recommendation').textContent = recommendation;
}

// Auto-run on page load
simulateVitals();

