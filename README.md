# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 375
- HTTP: 69 alive / 50 gold
- HTTPS: 58 alive / 12 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 174 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43510
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
