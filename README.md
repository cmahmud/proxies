# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 397
- HTTP: 93 alive / 70 gold
- HTTPS: 29 alive / 13 gold
- SOCKS4: 175 alive / 152 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48245
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
