# SyndProxy private pool

## Current pool

- Alive now: 1434
- Gold now: 425
- HTTP: 543 alive / 111 gold
- HTTPS: 332 alive / 21 gold
- SOCKS4: 238 alive / 138 gold
- SOCKS5: 321 alive / 155 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22674
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
