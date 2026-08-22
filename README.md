# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 396
- HTTP: 285 alive / 81 gold
- HTTPS: 165 alive / 22 gold
- SOCKS4: 224 alive / 149 gold
- SOCKS5: 237 alive / 144 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32377
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
