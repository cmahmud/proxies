# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 387
- HTTP: 207 alive / 79 gold
- HTTPS: 229 alive / 20 gold
- SOCKS4: 200 alive / 141 gold
- SOCKS5: 210 alive / 147 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26513
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
