# SyndProxy private pool

## Current pool

- Alive now: 1185
- Gold now: 411
- HTTP: 391 alive / 81 gold
- HTTPS: 267 alive / 16 gold
- SOCKS4: 263 alive / 151 gold
- SOCKS5: 264 alive / 163 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20631
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
