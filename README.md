# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 379
- HTTP: 90 alive / 58 gold
- HTTPS: 58 alive / 21 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 162 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43645
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
