function HealthCard({ score }) {

  return (
    <div>
      <h2>
        Health Score
      </h2>

      <h1>
        {score.health_score}
      </h1>

      <h3>
        {score.health_label}
      </h3>
    </div>
  );
}

export default HealthCard;
<HealthCard
  score={data.health_score}
/>