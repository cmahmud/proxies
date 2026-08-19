# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 549
- HTTP: 418 alive / 170 gold
- HTTPS: 357 alive / 84 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 207 alive / 148 gold

## Historical pool

- Discovered: 127333
- Ever alive: 19756
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
