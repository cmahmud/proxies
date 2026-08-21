# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 407
- HTTP: 376 alive / 108 gold
- HTTPS: 273 alive / 27 gold
- SOCKS4: 247 alive / 151 gold
- SOCKS5: 207 alive / 121 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30597
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
