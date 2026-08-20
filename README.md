# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 386
- HTTP: 230 alive / 82 gold
- HTTPS: 150 alive / 18 gold
- SOCKS4: 208 alive / 141 gold
- SOCKS5: 201 alive / 145 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25232
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
