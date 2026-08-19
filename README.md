# SyndProxy private pool

## Current pool

- Alive now: 1219
- Gold now: 407
- HTTP: 408 alive / 93 gold
- HTTPS: 263 alive / 15 gold
- SOCKS4: 239 alive / 150 gold
- SOCKS5: 309 alive / 149 gold

## Historical pool

- Discovered: 131840
- Ever alive: 21165
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
