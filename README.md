# SyndProxy private pool

## Current pool

- Alive now: 1519
- Gold now: 585
- HTTP: 571 alive / 198 gold
- HTTPS: 399 alive / 99 gold
- SOCKS4: 250 alive / 138 gold
- SOCKS5: 299 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23320
- Ever gold: 917

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
