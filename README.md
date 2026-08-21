# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 394
- HTTP: 298 alive / 83 gold
- HTTPS: 166 alive / 20 gold
- SOCKS4: 236 alive / 148 gold
- SOCKS5: 229 alive / 143 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29627
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
