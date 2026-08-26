# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 408
- HTTP: 104 alive / 63 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38615
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
