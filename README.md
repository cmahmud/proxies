# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 560
- HTTP: 350 alive / 166 gold
- HTTPS: 246 alive / 89 gold
- SOCKS4: 236 alive / 149 gold
- SOCKS5: 229 alive / 156 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19187
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
