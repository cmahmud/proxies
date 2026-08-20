# SyndProxy private pool

## Current pool

- Alive now: 1361
- Gold now: 581
- HTTP: 473 alive / 190 gold
- HTTPS: 343 alive / 101 gold
- SOCKS4: 226 alive / 134 gold
- SOCKS5: 319 alive / 156 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23217
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
