# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 402
- HTTP: 305 alive / 93 gold
- HTTPS: 236 alive / 25 gold
- SOCKS4: 246 alive / 155 gold
- SOCKS5: 217 alive / 129 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30835
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
