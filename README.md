# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 556
- HTTP: 407 alive / 168 gold
- HTTPS: 293 alive / 133 gold
- SOCKS4: 191 alive / 125 gold
- SOCKS5: 195 alive / 130 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19966
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
