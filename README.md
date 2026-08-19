# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 532
- HTTP: 392 alive / 159 gold
- HTTPS: 279 alive / 91 gold
- SOCKS4: 206 alive / 136 gold
- SOCKS5: 217 alive / 146 gold

## Historical pool

- Discovered: 122388
- Ever alive: 18683
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
