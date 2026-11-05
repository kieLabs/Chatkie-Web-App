export default function Home() {
  return (
    <html>
      <head>
        <title>ChatKie</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>

      <body style={{
        margin: 0,
        padding: 0,
        width: "100%",
        height: "100dvh",
        overflow: "hidden"
      }}>
        <iframe
          src="/ChatKie/legacy.html"
          title="ChatKie"
          style={{
            width: "100%",
            height: "100%",
            border: "none",
            display: "block"
          }}
        />
      </body>
    </html>
  );
}
