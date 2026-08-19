# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 342
- HTTP: 350 alive / 65 gold
- HTTPS: 214 alive / 15 gold
- SOCKS4: 249 alive / 137 gold
- SOCKS5: 213 alive / 125 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15339
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
