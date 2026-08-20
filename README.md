# SyndProxy private pool

## Current pool

- Alive now: 815
- Gold now: 398
- HTTP: 215 alive / 78 gold
- HTTPS: 179 alive / 20 gold
- SOCKS4: 208 alive / 149 gold
- SOCKS5: 213 alive / 151 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26500
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
