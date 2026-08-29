# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 388
- HTTP: 91 alive / 66 gold
- HTTPS: 70 alive / 17 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 165 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43372
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
