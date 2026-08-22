# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 407
- HTTP: 277 alive / 88 gold
- HTTPS: 191 alive / 22 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 245 alive / 156 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31967
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
