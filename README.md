# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 238
- HTTP: 230 alive / 30 gold
- HTTPS: 114 alive / 8 gold
- SOCKS4: 234 alive / 111 gold
- SOCKS5: 195 alive / 89 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6880
- Ever gold: 323

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
