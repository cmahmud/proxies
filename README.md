# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 409
- HTTP: 250 alive / 89 gold
- HTTPS: 186 alive / 22 gold
- SOCKS4: 207 alive / 142 gold
- SOCKS5: 239 alive / 156 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27799
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
