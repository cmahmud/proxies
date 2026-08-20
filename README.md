# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 383
- HTTP: 265 alive / 72 gold
- HTTPS: 180 alive / 15 gold
- SOCKS4: 211 alive / 149 gold
- SOCKS5: 208 alive / 147 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26479
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
