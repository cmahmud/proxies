# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 315
- HTTP: 313 alive / 53 gold
- HTTPS: 201 alive / 10 gold
- SOCKS4: 205 alive / 126 gold
- SOCKS5: 200 alive / 126 gold

## Historical pool

- Discovered: 129252
- Ever alive: 20138
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
