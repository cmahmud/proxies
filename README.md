# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 395
- HTTP: 212 alive / 83 gold
- HTTPS: 116 alive / 19 gold
- SOCKS4: 215 alive / 142 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 147690
- Ever alive: 25972
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
