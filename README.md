# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 203
- HTTP: 369 alive / 22 gold
- HTTPS: 166 alive / 9 gold
- SOCKS4: 240 alive / 101 gold
- SOCKS5: 207 alive / 71 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8336
- Ever gold: 348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
