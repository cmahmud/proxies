# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 273
- HTTP: 239 alive / 27 gold
- HTTPS: 152 alive / 5 gold
- SOCKS4: 226 alive / 134 gold
- SOCKS5: 206 alive / 107 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12455
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
