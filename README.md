# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 422
- HTTP: 275 alive / 87 gold
- HTTPS: 183 alive / 27 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 269 alive / 160 gold

## Historical pool

- Discovered: 164932
- Ever alive: 32179
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
