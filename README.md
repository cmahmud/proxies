# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 412
- HTTP: 363 alive / 108 gold
- HTTPS: 247 alive / 27 gold
- SOCKS4: 240 alive / 151 gold
- SOCKS5: 204 alive / 126 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30588
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
