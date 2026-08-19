# SyndProxy private pool

## Current pool

- Alive now: 1435
- Gold now: 418
- HTTP: 536 alive / 91 gold
- HTTPS: 353 alive / 18 gold
- SOCKS4: 258 alive / 152 gold
- SOCKS5: 288 alive / 157 gold

## Historical pool

- Discovered: 131815
- Ever alive: 20859
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
