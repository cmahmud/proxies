# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 393
- HTTP: 226 alive / 78 gold
- HTTPS: 186 alive / 18 gold
- SOCKS4: 208 alive / 148 gold
- SOCKS5: 213 alive / 149 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26490
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
