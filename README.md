# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 298
- HTTP: 282 alive / 23 gold
- HTTPS: 202 alive / 4 gold
- SOCKS4: 246 alive / 148 gold
- SOCKS5: 241 alive / 123 gold

## Historical pool

- Discovered: 102812
- Ever alive: 12773
- Ever gold: 404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
