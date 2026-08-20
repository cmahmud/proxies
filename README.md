# SyndProxy private pool

## Current pool

- Alive now: 722
- Gold now: 364
- HTTP: 191 alive / 69 gold
- HTTPS: 142 alive / 18 gold
- SOCKS4: 185 alive / 135 gold
- SOCKS5: 204 alive / 142 gold

## Historical pool

- Discovered: 149498
- Ever alive: 26698
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
