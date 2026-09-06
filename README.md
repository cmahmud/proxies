# SyndProxy validated proxy pool

## Current pool

- Alive now: 428
- Gold now: 351
- HTTP: 80 alive / 66 gold
- HTTPS: 28 alive / 12 gold
- SOCKS4: 155 alive / 136 gold
- SOCKS5: 165 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48397
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
