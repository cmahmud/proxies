# SyndProxy private pool

## Current pool

- Alive now: 1984
- Gold now: 651
- HTTP: 789 alive / 223 gold
- HTTPS: 623 alive / 119 gold
- SOCKS4: 249 alive / 145 gold
- SOCKS5: 323 alive / 164 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24346
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
