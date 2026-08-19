# SyndProxy private pool

## Current pool

- Alive now: 1254
- Gold now: 508
- HTTP: 459 alive / 165 gold
- HTTPS: 343 alive / 47 gold
- SOCKS4: 225 alive / 147 gold
- SOCKS5: 227 alive / 149 gold

## Historical pool

- Discovered: 125701
- Ever alive: 19680
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
