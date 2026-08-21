# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 407
- HTTP: 269 alive / 97 gold
- HTTPS: 219 alive / 36 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 257 alive / 132 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30927
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
