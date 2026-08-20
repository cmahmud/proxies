# SyndProxy private pool

## Current pool

- Alive now: 1379
- Gold now: 584
- HTTP: 486 alive / 194 gold
- HTTPS: 366 alive / 100 gold
- SOCKS4: 251 alive / 141 gold
- SOCKS5: 276 alive / 149 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23294
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
