# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 406
- HTTP: 336 alive / 95 gold
- HTTPS: 250 alive / 15 gold
- SOCKS4: 249 alive / 148 gold
- SOCKS5: 312 alive / 148 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21094
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
