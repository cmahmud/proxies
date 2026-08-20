# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 401
- HTTP: 195 alive / 84 gold
- HTTPS: 128 alive / 23 gold
- SOCKS4: 190 alive / 127 gold
- SOCKS5: 226 alive / 167 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27109
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
