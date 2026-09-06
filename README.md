# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 403
- HTTP: 134 alive / 82 gold
- HTTPS: 60 alive / 27 gold
- SOCKS4: 165 alive / 141 gold
- SOCKS5: 184 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48039
- Ever gold: 1514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
