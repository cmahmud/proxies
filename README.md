# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 371
- HTTP: 282 alive / 86 gold
- HTTPS: 225 alive / 27 gold
- SOCKS4: 192 alive / 120 gold
- SOCKS5: 223 alive / 138 gold

## Historical pool

- Discovered: 153750
- Ever alive: 28838
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
