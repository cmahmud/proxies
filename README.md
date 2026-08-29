# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 394
- HTTP: 85 alive / 63 gold
- HTTPS: 92 alive / 18 gold
- SOCKS4: 162 alive / 153 gold
- SOCKS5: 167 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43336
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
