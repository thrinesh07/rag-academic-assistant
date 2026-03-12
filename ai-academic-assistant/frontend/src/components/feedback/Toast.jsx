import { useEffect } from "react";

export default function Toast({
  show,
  message,
  variant = "success",
  onClose,
  duration = 3000
}) {
  useEffect(() => {
    if (!show) return;

    const timer = setTimeout(() => {
      onClose?.();
    }, duration);

    return () => clearTimeout(timer);
  }, [show, duration, onClose]);

  if (!show) return null;

  return (
    <div
      className="position-fixed bottom-0 end-0 p-3"
      style={{ zIndex: 1055 }}
    >
      <div className={`toast show text-white bg-${variant}`}>
        <div className="d-flex">
          <div className="toast-body">
            {message}
          </div>

          <button
            type="button"
            className="btn-close btn-close-white me-2 m-auto"
            onClick={onClose}
          />
        </div>
      </div>
    </div>
  );
}