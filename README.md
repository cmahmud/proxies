# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 407
- HTTP: 132 alive / 71 gold
- HTTPS: 167 alive / 20 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40429
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
