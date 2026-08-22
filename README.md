# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 437
- HTTP: 326 alive / 96 gold
- HTTPS: 219 alive / 32 gold
- SOCKS4: 207 alive / 140 gold
- SOCKS5: 273 alive / 169 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31268
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
