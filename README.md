# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 399
- HTTP: 179 alive / 76 gold
- HTTPS: 135 alive / 20 gold
- SOCKS4: 201 alive / 154 gold
- SOCKS5: 210 alive / 149 gold

## Historical pool

- Discovered: 149503
- Ever alive: 26757
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
