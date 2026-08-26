# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 403
- HTTP: 102 alive / 61 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39035
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
