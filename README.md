# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 321
- HTTP: 275 alive / 59 gold
- HTTPS: 170 alive / 13 gold
- SOCKS4: 196 alive / 126 gold
- SOCKS5: 201 alive / 123 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20047
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
