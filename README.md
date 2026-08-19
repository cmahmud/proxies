# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 512
- HTTP: 342 alive / 146 gold
- HTTPS: 230 alive / 89 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 207 alive / 129 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17629
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
