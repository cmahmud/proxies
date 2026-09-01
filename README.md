# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 425
- HTTP: 112 alive / 66 gold
- HTTPS: 72 alive / 30 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47056
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
