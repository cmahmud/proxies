# SyndProxy private pool

## Current pool

- Alive now: 1243
- Gold now: 434
- HTTP: 407 alive / 104 gold
- HTTPS: 311 alive / 25 gold
- SOCKS4: 267 alive / 151 gold
- SOCKS5: 258 alive / 154 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25151
- Ever gold: 1055

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
