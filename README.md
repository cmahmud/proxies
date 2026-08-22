# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 398
- HTTP: 267 alive / 87 gold
- HTTPS: 199 alive / 28 gold
- SOCKS4: 218 alive / 136 gold
- SOCKS5: 242 alive / 147 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31974
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
