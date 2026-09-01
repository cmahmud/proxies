# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 425
- HTTP: 102 alive / 68 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47044
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
