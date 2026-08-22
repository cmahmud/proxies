# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 410
- HTTP: 196 alive / 87 gold
- HTTPS: 127 alive / 24 gold
- SOCKS4: 199 alive / 142 gold
- SOCKS5: 222 alive / 157 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31962
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
