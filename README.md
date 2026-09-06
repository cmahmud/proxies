# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 397
- HTTP: 92 alive / 64 gold
- HTTPS: 32 alive / 12 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48252
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
