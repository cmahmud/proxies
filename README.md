# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 313
- HTTP: 307 alive / 53 gold
- HTTPS: 197 alive / 10 gold
- SOCKS4: 209 alive / 126 gold
- SOCKS5: 199 alive / 124 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20137
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
