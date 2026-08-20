# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 395
- HTTP: 250 alive / 82 gold
- HTTPS: 118 alive / 20 gold
- SOCKS4: 217 alive / 142 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 147690
- Ever alive: 25977
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
