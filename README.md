# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 456
- HTTP: 128 alive / 85 gold
- HTTPS: 116 alive / 39 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 205 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44786
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
