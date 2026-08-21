# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 403
- HTTP: 252 alive / 88 gold
- HTTPS: 150 alive / 20 gold
- SOCKS4: 207 alive / 137 gold
- SOCKS5: 216 alive / 158 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27630
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
