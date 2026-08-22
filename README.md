# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 422
- HTTP: 288 alive / 85 gold
- HTTPS: 195 alive / 29 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 264 alive / 160 gold

## Historical pool

- Discovered: 164928
- Ever alive: 32172
- Ever gold: 1172

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
