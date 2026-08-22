# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 378
- HTTP: 226 alive / 84 gold
- HTTPS: 143 alive / 23 gold
- SOCKS4: 203 alive / 114 gold
- SOCKS5: 249 alive / 157 gold

## Historical pool

- Discovered: 166560
- Ever alive: 32402
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
