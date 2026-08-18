# SyndProxy private pool

## Current pool

- Alive now: 634
- Gold now: 235
- HTTP: 174 alive / 29 gold
- HTTPS: 77 alive / 9 gold
- SOCKS4: 193 alive / 115 gold
- SOCKS5: 190 alive / 82 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7601
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
