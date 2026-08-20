# SyndProxy private pool

## Current pool

- Alive now: 1748
- Gold now: 655
- HTTP: 677 alive / 213 gold
- HTTPS: 506 alive / 116 gold
- SOCKS4: 239 alive / 159 gold
- SOCKS5: 326 alive / 167 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23930
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
