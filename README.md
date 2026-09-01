# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 427
- HTTP: 105 alive / 74 gold
- HTTPS: 72 alive / 26 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47051
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
