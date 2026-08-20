# SyndProxy private pool

## Current pool

- Alive now: 876
- Gold now: 374
- HTTP: 250 alive / 78 gold
- HTTPS: 169 alive / 23 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 246 alive / 137 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25287
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
