# SyndProxy private pool

## Current pool

- Alive now: 1192
- Gold now: 429
- HTTP: 430 alive / 106 gold
- HTTPS: 292 alive / 29 gold
- SOCKS4: 232 alive / 151 gold
- SOCKS5: 238 alive / 143 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30515
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
