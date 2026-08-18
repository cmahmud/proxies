# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 281
- HTTP: 306 alive / 28 gold
- HTTPS: 119 alive / 5 gold
- SOCKS4: 243 alive / 140 gold
- SOCKS5: 231 alive / 108 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12263
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
