# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 409
- HTTP: 195 alive / 89 gold
- HTTPS: 127 alive / 26 gold
- SOCKS4: 192 alive / 138 gold
- SOCKS5: 239 alive / 156 gold

## Historical pool

- Discovered: 163377
- Ever alive: 31908
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
