# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 423
- HTTP: 107 alive / 70 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47047
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
