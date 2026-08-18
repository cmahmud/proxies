# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 336
- HTTP: 262 alive / 66 gold
- HTTPS: 196 alive / 13 gold
- SOCKS4: 222 alive / 141 gold
- SOCKS5: 204 alive / 116 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15223
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
