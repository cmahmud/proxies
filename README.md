# SyndProxy private pool

## Current pool

- Alive now: 1530
- Gold now: 393
- HTTP: 554 alive / 104 gold
- HTTPS: 402 alive / 20 gold
- SOCKS4: 255 alive / 124 gold
- SOCKS5: 319 alive / 145 gold

## Historical pool

- Discovered: 136221
- Ever alive: 22489
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
