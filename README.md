# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 418
- HTTP: 227 alive / 84 gold
- HTTPS: 166 alive / 29 gold
- SOCKS4: 212 alive / 139 gold
- SOCKS5: 241 alive / 166 gold

## Historical pool

- Discovered: 163879
- Ever alive: 32032
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
