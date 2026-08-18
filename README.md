# SyndProxy private pool

## Current pool

- Alive now: 658
- Gold now: 252
- HTTP: 217 alive / 29 gold
- HTTPS: 87 alive / 10 gold
- SOCKS4: 178 alive / 127 gold
- SOCKS5: 176 alive / 86 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9742
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
