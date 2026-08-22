# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 431
- HTTP: 304 alive / 94 gold
- HTTPS: 216 alive / 27 gold
- SOCKS4: 209 alive / 143 gold
- SOCKS5: 249 alive / 167 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31245
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
