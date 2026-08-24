# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 401
- HTTP: 115 alive / 68 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 177314
- Ever alive: 33278
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
