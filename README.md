# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 347
- HTTP: 82 alive / 60 gold
- HTTPS: 32 alive / 13 gold
- SOCKS4: 143 alive / 138 gold
- SOCKS5: 166 alive / 136 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48403
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
