# SyndProxy private pool

## Current pool

- Alive now: 1646
- Gold now: 609
- HTTP: 594 alive / 218 gold
- HTTPS: 469 alive / 112 gold
- SOCKS4: 214 alive / 135 gold
- SOCKS5: 369 alive / 144 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23904
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
