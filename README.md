# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 450
- HTTP: 131 alive / 80 gold
- HTTPS: 95 alive / 36 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 220 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45363
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
