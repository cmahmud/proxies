# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 408
- HTTP: 232 alive / 91 gold
- HTTPS: 143 alive / 18 gold
- SOCKS4: 191 alive / 147 gold
- SOCKS5: 219 alive / 152 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27843
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
