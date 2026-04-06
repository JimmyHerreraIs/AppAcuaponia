import Navbar from "../components/Navbar";
import Card from "../components/Card";
import Chart from "../components/Chart";
import Alerts from "../components/Alerts";
import ControlPanel from "../components/ControlPanel";

export default function Dashboard() {
  return (
    <div>
      <Navbar />

      {/* CARDS SUPERIORES */}
      <div className="grid grid-cols-4 gap-4">
        <Card title="Temperature" value="25.3°C" />
        <Card title="pH Level" value="7.2" />
        <Card title="Feeding Status" value="Automatic" />
        <Card title="Luz recibida ayer" value="5h natural / 3h LED" />
      </div>

      {/* GRÁFICO */}
      <Chart />

      {/* CONTROL + ALERTAS */}
      <div className="grid grid-cols-2 gap-4">
        <ControlPanel />
        <Alerts />
      </div>
    </div>
  );
}