# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 435
- HTTP: 115 alive / 76 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47572
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
