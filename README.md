# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 423
- HTTP: 92 alive / 69 gold
- HTTPS: 95 alive / 29 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47265
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
