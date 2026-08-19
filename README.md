# SyndProxy private pool

## Current pool

- Alive now: 857
- Gold now: 340
- HTTP: 286 alive / 61 gold
- HTTPS: 185 alive / 12 gold
- SOCKS4: 204 alive / 143 gold
- SOCKS5: 182 alive / 124 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20175
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
