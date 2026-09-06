# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 397
- HTTP: 103 alive / 75 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 174 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48093
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
