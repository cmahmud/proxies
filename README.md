# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 423
- HTTP: 99 alive / 67 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47057
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
