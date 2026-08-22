# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 405
- HTTP: 209 alive / 83 gold
- HTTPS: 136 alive / 28 gold
- SOCKS4: 202 alive / 130 gold
- SOCKS5: 238 alive / 164 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31498
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
