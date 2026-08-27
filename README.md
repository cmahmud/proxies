# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 391
- HTTP: 76 alive / 48 gold
- HTTPS: 55 alive / 14 gold
- SOCKS4: 177 alive / 165 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41616
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
