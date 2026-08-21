# SyndProxy private pool

## Current pool

- Alive now: 1102
- Gold now: 447
- HTTP: 341 alive / 98 gold
- HTTPS: 258 alive / 31 gold
- SOCKS4: 248 alive / 163 gold
- SOCKS5: 255 alive / 155 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30264
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
