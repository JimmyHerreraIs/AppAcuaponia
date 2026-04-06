import {LineChart, Line, XAxis, Tooltip, Legend} from "recharts";

const data=[
    { time:"10am", temp: 19, ph: 6.8, light:5},
    { time: "12PM", temp: 22, ph: 7.0, light: 8 },
    { time: "2PM", temp: 25, ph: 7.2, light: 10 },
    { time: "4PM", temp: 27, ph: 7.1, light: 7 },
];

export default function Chart(){
    return(
    <LineChart width={600} height={300} data={data}>
      <XAxis dataKey="time" />
      <YAxis />
      <Tooltip />
      <Legend />

      <Line type="monotone" dataKey="temp" stroke="#ff7300" />
      <Line type="monotone" dataKey="ph" stroke="#387908" />
      <Line type="monotone" dataKey="light" stroke="#FFD700" /> {/* 🟡 */}
    </LineChart>
    );
}