# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 291
- HTTP: 110 alive / 72 gold
- HTTPS: 41 alive / 20 gold
- SOCKS4: 76 alive / 66 gold
- SOCKS5: 155 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47868
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
