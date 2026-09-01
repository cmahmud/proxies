# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 423
- HTTP: 105 alive / 69 gold
- HTTPS: 72 alive / 25 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47045
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
