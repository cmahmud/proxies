# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 377
- HTTP: 210 alive / 72 gold
- HTTPS: 98 alive / 17 gold
- SOCKS4: 230 alive / 144 gold
- SOCKS5: 205 alive / 144 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25430
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
