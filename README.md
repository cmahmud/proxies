# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 461
- HTTP: 140 alive / 89 gold
- HTTPS: 142 alive / 36 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 226 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45855
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
