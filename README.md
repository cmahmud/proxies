# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 321
- HTTP: 252 alive / 60 gold
- HTTPS: 176 alive / 14 gold
- SOCKS4: 201 alive / 125 gold
- SOCKS5: 206 alive / 122 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20059
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
