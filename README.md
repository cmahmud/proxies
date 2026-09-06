# SyndProxy validated proxy pool

## Current pool

- Alive now: 397
- Gold now: 308
- HTTP: 73 alive / 47 gold
- HTTPS: 32 alive / 9 gold
- SOCKS4: 147 alive / 133 gold
- SOCKS5: 145 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48321
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
