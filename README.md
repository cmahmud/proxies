# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 385
- HTTP: 225 alive / 82 gold
- HTTPS: 125 alive / 19 gold
- SOCKS4: 220 alive / 136 gold
- SOCKS5: 224 alive / 148 gold

## Historical pool

- Discovered: 157429
- Ever alive: 29763
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
