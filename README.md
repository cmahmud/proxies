# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 268
- HTTP: 222 alive / 26 gold
- HTTPS: 129 alive / 2 gold
- SOCKS4: 219 alive / 136 gold
- SOCKS5: 198 alive / 104 gold

## Historical pool

- Discovered: 99079
- Ever alive: 11472
- Ever gold: 384

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
