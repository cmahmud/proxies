# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 260
- HTTP: 275 alive / 30 gold
- HTTPS: 122 alive / 4 gold
- SOCKS4: 208 alive / 118 gold
- SOCKS5: 213 alive / 108 gold

## Historical pool

- Discovered: 99142
- Ever alive: 11986
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
