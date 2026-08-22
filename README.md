# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 431
- HTTP: 297 alive / 93 gold
- HTTPS: 216 alive / 29 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 254 alive / 166 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31245
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
