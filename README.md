# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 386
- HTTP: 192 alive / 76 gold
- HTTPS: 157 alive / 27 gold
- SOCKS4: 206 alive / 127 gold
- SOCKS5: 208 alive / 156 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27061
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
