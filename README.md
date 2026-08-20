# SyndProxy private pool

## Current pool

- Alive now: 1643
- Gold now: 613
- HTTP: 597 alive / 217 gold
- HTTPS: 475 alive / 113 gold
- SOCKS4: 209 alive / 135 gold
- SOCKS5: 362 alive / 148 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23915
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
