# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 397
- HTTP: 125 alive / 80 gold
- HTTPS: 59 alive / 25 gold
- SOCKS4: 163 alive / 139 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48036
- Ever gold: 1514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
