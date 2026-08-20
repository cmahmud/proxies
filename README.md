# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 398
- HTTP: 342 alive / 75 gold
- HTTPS: 201 alive / 20 gold
- SOCKS4: 211 alive / 153 gold
- SOCKS5: 227 alive / 150 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26794
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
