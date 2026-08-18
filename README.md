# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 310
- HTTP: 285 alive / 40 gold
- HTTPS: 192 alive / 9 gold
- SOCKS4: 239 alive / 133 gold
- SOCKS5: 217 alive / 128 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14266
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
