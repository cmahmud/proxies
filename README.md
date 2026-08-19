# SyndProxy private pool

## Current pool

- Alive now: 1274
- Gold now: 532
- HTTP: 472 alive / 182 gold
- HTTPS: 340 alive / 60 gold
- SOCKS4: 216 alive / 123 gold
- SOCKS5: 246 alive / 167 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19661
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
