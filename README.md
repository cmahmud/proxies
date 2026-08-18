# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 244
- HTTP: 391 alive / 31 gold
- HTTPS: 133 alive / 6 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 156 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13646
- Ever gold: 428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
