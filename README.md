# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 342
- HTTP: 76 alive / 62 gold
- HTTPS: 28 alive / 10 gold
- SOCKS4: 155 alive / 136 gold
- SOCKS5: 164 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48397
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
