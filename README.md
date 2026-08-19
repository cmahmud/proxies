# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 317
- HTTP: 260 alive / 56 gold
- HTTPS: 187 alive / 9 gold
- SOCKS4: 196 alive / 124 gold
- SOCKS5: 208 alive / 128 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20133
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
