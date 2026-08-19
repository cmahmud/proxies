# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 530
- HTTP: 401 alive / 157 gold
- HTTPS: 266 alive / 90 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 208 alive / 145 gold

## Historical pool

- Discovered: 127355
- Ever alive: 19889
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
