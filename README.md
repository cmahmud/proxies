# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 393
- HTTP: 285 alive / 86 gold
- HTTPS: 190 alive / 23 gold
- SOCKS4: 217 alive / 136 gold
- SOCKS5: 257 alive / 148 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31970
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
