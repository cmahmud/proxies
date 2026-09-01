# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 423
- HTTP: 98 alive / 67 gold
- HTTPS: 69 alive / 27 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47062
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
