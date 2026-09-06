# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 397
- HTTP: 109 alive / 75 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 183 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48227
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
