# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 343
- HTTP: 84 alive / 63 gold
- HTTPS: 31 alive / 15 gold
- SOCKS4: 152 alive / 134 gold
- SOCKS5: 164 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48397
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
