# SyndProxy private pool

## Current pool

- Alive now: 617
- Gold now: 266
- HTTP: 171 alive / 33 gold
- HTTPS: 78 alive / 10 gold
- SOCKS4: 190 alive / 140 gold
- SOCKS5: 178 alive / 83 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9687
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
