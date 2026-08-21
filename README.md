# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 407
- HTTP: 334 alive / 95 gold
- HTTPS: 273 alive / 36 gold
- SOCKS4: 230 alive / 145 gold
- SOCKS5: 224 alive / 131 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30986
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
