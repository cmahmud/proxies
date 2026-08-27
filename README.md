# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 411
- HTTP: 90 alive / 58 gold
- HTTPS: 93 alive / 22 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 198 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41493
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
