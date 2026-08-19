# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 517
- HTTP: 348 alive / 149 gold
- HTTPS: 240 alive / 92 gold
- SOCKS4: 212 alive / 148 gold
- SOCKS5: 200 alive / 128 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17613
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
