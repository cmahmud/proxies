# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 464
- HTTP: 287 alive / 118 gold
- HTTPS: 207 alive / 86 gold
- SOCKS4: 190 alive / 124 gold
- SOCKS5: 216 alive / 136 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17495
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
