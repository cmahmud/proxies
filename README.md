# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 404
- HTTP: 294 alive / 91 gold
- HTTPS: 184 alive / 27 gold
- SOCKS4: 222 alive / 150 gold
- SOCKS5: 229 alive / 136 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32342
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
