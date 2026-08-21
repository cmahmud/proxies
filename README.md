# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 400
- HTTP: 251 alive / 80 gold
- HTTPS: 151 alive / 22 gold
- SOCKS4: 239 alive / 149 gold
- SOCKS5: 234 alive / 149 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29627
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
