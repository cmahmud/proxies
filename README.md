# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 375
- HTTP: 90 alive / 53 gold
- HTTPS: 42 alive / 22 gold
- SOCKS4: 155 alive / 151 gold
- SOCKS5: 160 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43643
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
