export default function Card({
  title,
  children,
  className = ""
}) {
  return (
    <div className={`card shadow-sm ${className}`}>
      {title && (
        <div className="card-header bg-white">
          <h6 className="mb-0 fw-semibold">{title}</h6>
        </div>
      )}

      <div className="card-body">
        {children}
      </div>
    </div>
  );
}