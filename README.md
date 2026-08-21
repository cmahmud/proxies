# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 404
- HTTP: 285 alive / 96 gold
- HTTPS: 206 alive / 36 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 253 alive / 130 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30920
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
