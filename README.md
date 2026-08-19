# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 301
- HTTP: 251 alive / 61 gold
- HTTPS: 177 alive / 8 gold
- SOCKS4: 191 alive / 97 gold
- SOCKS5: 191 alive / 135 gold

## Historical pool

- Discovered: 129263
- Ever alive: 20142
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
