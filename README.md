# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 427
- HTTP: 99 alive / 70 gold
- HTTPS: 65 alive / 28 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47056
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
