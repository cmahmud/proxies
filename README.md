# SyndProxy private pool

## Current pool

- Alive now: 1419
- Gold now: 585
- HTTP: 521 alive / 198 gold
- HTTPS: 376 alive / 99 gold
- SOCKS4: 235 alive / 138 gold
- SOCKS5: 287 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23316
- Ever gold: 917

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
