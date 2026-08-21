# SyndProxy private pool

## Current pool

- Alive now: 1408
- Gold now: 466
- HTTP: 512 alive / 107 gold
- HTTPS: 364 alive / 34 gold
- SOCKS4: 240 alive / 154 gold
- SOCKS5: 292 alive / 171 gold

## Historical pool

- Discovered: 159265
- Ever alive: 30355
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
