# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 366
- HTTP: 211 alive / 64 gold
- HTTPS: 116 alive / 19 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 209 alive / 141 gold

## Historical pool

- Discovered: 145551
- Ever alive: 25422
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
