# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 448
- HTTP: 405 alive / 108 gold
- HTTPS: 282 alive / 29 gold
- SOCKS4: 218 alive / 152 gold
- SOCKS5: 263 alive / 159 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28578
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
