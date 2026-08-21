# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 420
- HTTP: 295 alive / 85 gold
- HTTPS: 200 alive / 26 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28906
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
