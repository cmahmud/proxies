# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 358
- HTTP: 277 alive / 85 gold
- HTTPS: 169 alive / 19 gold
- SOCKS4: 202 alive / 142 gold
- SOCKS5: 179 alive / 112 gold

## Historical pool

- Discovered: 145270
- Ever alive: 25329
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
