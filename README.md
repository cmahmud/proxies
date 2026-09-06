# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 397
- HTTP: 100 alive / 68 gold
- HTTPS: 34 alive / 14 gold
- SOCKS4: 172 alive / 153 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48245
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
