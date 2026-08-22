# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 416
- HTTP: 207 alive / 94 gold
- HTTPS: 148 alive / 30 gold
- SOCKS4: 209 alive / 130 gold
- SOCKS5: 235 alive / 162 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31952
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
