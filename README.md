# SyndProxy private pool

## Current pool

- Alive now: 1703
- Gold now: 681
- HTTP: 645 alive / 261 gold
- HTTPS: 477 alive / 129 gold
- SOCKS4: 223 alive / 127 gold
- SOCKS5: 358 alive / 164 gold

## Historical pool

- Discovered: 143495
- Ever alive: 24823
- Ever gold: 1049

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
