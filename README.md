# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 417
- HTTP: 102 alive / 63 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35576
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
