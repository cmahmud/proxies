# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 407
- HTTP: 94 alive / 59 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 185 alive / 165 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41561
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
