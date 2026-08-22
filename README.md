# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 421
- HTTP: 291 alive / 87 gold
- HTTPS: 200 alive / 24 gold
- SOCKS4: 224 alive / 149 gold
- SOCKS5: 262 alive / 161 gold

## Historical pool

- Discovered: 164932
- Ever alive: 32182
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
