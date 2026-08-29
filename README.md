# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 382
- HTTP: 82 alive / 55 gold
- HTTPS: 73 alive / 11 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43475
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
