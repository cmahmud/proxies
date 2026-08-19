# SyndProxy private pool

## Current pool

- Alive now: 1238
- Gold now: 518
- HTTP: 473 alive / 182 gold
- HTTPS: 321 alive / 55 gold
- SOCKS4: 200 alive / 122 gold
- SOCKS5: 244 alive / 159 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19650
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
