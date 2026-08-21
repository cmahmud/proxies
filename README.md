# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 407
- HTTP: 236 alive / 91 gold
- HTTPS: 155 alive / 21 gold
- SOCKS4: 205 alive / 136 gold
- SOCKS5: 227 alive / 159 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27642
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
