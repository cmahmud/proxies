# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 407
- HTTP: 274 alive / 83 gold
- HTTPS: 157 alive / 27 gold
- SOCKS4: 238 alive / 152 gold
- SOCKS5: 236 alive / 145 gold

## Historical pool

- Discovered: 166318
- Ever alive: 32382
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
