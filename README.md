# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 399
- HTTP: 177 alive / 76 gold
- HTTPS: 150 alive / 21 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 209 alive / 152 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26951
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
