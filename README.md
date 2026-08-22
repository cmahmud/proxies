# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 418
- HTTP: 316 alive / 87 gold
- HTTPS: 186 alive / 25 gold
- SOCKS4: 232 alive / 148 gold
- SOCKS5: 274 alive / 158 gold

## Historical pool

- Discovered: 164932
- Ever alive: 32185
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
