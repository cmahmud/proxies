# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 534
- HTTP: 337 alive / 162 gold
- HTTPS: 235 alive / 89 gold
- SOCKS4: 231 alive / 152 gold
- SOCKS5: 202 alive / 131 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18081
- Ever gold: 715

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
