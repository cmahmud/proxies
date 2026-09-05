# SyndProxy validated proxy pool

## Current pool

- Alive now: 426
- Gold now: 319
- HTTP: 108 alive / 75 gold
- HTTPS: 58 alive / 23 gold
- SOCKS4: 95 alive / 81 gold
- SOCKS5: 165 alive / 140 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47947
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
