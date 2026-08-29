# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 378
- HTTP: 95 alive / 54 gold
- HTTPS: 40 alive / 22 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 161 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43643
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
