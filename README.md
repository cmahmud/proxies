# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 408
- HTTP: 111 alive / 63 gold
- HTTPS: 140 alive / 19 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41363
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
