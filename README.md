# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 388
- HTTP: 219 alive / 75 gold
- HTTPS: 193 alive / 17 gold
- SOCKS4: 208 alive / 149 gold
- SOCKS5: 209 alive / 147 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26487
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
