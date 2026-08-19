# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 320
- HTTP: 258 alive / 57 gold
- HTTPS: 177 alive / 13 gold
- SOCKS4: 192 alive / 125 gold
- SOCKS5: 207 alive / 125 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20058
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
