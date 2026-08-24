# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 403
- HTTP: 111 alive / 69 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 177314
- Ever alive: 33278
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
