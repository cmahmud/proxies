# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 411
- HTTP: 185 alive / 88 gold
- HTTPS: 131 alive / 24 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 223 alive / 158 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31961
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
