export default function RetrievedContext({ chunks = [] }) {

  if (!chunks.length) return null;

  return (
    <details className="mt-2">
      <summary className="small text-muted">
        View retrieved context
      </summary>

      <ul className="small mt-2 ps-3">
        {chunks.map((chunk, index) => (
          <li key={index}>
            {chunk.text?.slice(0, 150)}...
          </li>
        ))}
      </ul>

    </details>
  );
}