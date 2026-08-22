# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 423
- HTTP: 314 alive / 79 gold
- HTTPS: 225 alive / 28 gold
- SOCKS4: 228 alive / 141 gold
- SOCKS5: 267 alive / 175 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32230
- Ever gold: 1176

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
