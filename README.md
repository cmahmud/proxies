# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 424
- HTTP: 125 alive / 69 gold
- HTTPS: 75 alive / 28 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47054
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
