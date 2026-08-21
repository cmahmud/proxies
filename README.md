# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 400
- HTTP: 215 alive / 86 gold
- HTTPS: 128 alive / 24 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 231 alive / 142 gold

## Historical pool

- Discovered: 155686
- Ever alive: 29217
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
