# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 410
- HTTP: 219 alive / 89 gold
- HTTPS: 168 alive / 25 gold
- SOCKS4: 207 alive / 131 gold
- SOCKS5: 227 alive / 165 gold

## Historical pool

- Discovered: 151684
- Ever alive: 27706
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
