# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 416
- HTTP: 363 alive / 113 gold
- HTTPS: 250 alive / 28 gold
- SOCKS4: 243 alive / 151 gold
- SOCKS5: 207 alive / 124 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30582
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
