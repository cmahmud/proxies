# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 323
- HTTP: 255 alive / 58 gold
- HTTPS: 180 alive / 9 gold
- SOCKS4: 190 alive / 127 gold
- SOCKS5: 192 alive / 129 gold

## Historical pool

- Discovered: 129259
- Ever alive: 20141
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
