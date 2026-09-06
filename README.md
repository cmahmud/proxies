# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 397
- HTTP: 97 alive / 63 gold
- HTTPS: 30 alive / 13 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48252
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
