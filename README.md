# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 404
- HTTP: 119 alive / 68 gold
- HTTPS: 54 alive / 13 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 195 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33330
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
