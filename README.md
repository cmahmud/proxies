# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 404
- HTTP: 288 alive / 94 gold
- HTTPS: 190 alive / 26 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 208 alive / 136 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32343
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
