# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 304
- HTTP: 362 alive / 28 gold
- HTTPS: 145 alive / 6 gold
- SOCKS4: 228 alive / 142 gold
- SOCKS5: 219 alive / 128 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13350
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
