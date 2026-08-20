# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 397
- HTTP: 220 alive / 79 gold
- HTTPS: 182 alive / 20 gold
- SOCKS4: 208 alive / 149 gold
- SOCKS5: 216 alive / 149 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26490
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
