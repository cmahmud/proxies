# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 408
- HTTP: 216 alive / 89 gold
- HTTPS: 98 alive / 17 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 236 alive / 153 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29286
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
