# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 246
- HTTP: 385 alive / 25 gold
- HTTPS: 98 alive / 10 gold
- SOCKS4: 181 alive / 124 gold
- SOCKS5: 182 alive / 87 gold

## Historical pool

- Discovered: 94370
- Ever alive: 9942
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
