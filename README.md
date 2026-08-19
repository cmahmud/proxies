# SyndProxy private pool

## Current pool

- Alive now: 857
- Gold now: 321
- HTTP: 258 alive / 59 gold
- HTTPS: 169 alive / 15 gold
- SOCKS4: 200 alive / 126 gold
- SOCKS5: 230 alive / 121 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20086
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
