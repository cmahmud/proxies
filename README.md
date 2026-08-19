# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 319
- HTTP: 309 alive / 57 gold
- HTTPS: 178 alive / 11 gold
- SOCKS4: 192 alive / 124 gold
- SOCKS5: 208 alive / 127 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20049
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
