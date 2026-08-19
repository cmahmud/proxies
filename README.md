# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 305
- HTTP: 292 alive / 63 gold
- HTTPS: 226 alive / 19 gold
- SOCKS4: 185 alive / 117 gold
- SOCKS5: 191 alive / 106 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15458
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
