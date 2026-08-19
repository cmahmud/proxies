# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 341
- HTTP: 350 alive / 59 gold
- HTTPS: 194 alive / 16 gold
- SOCKS4: 212 alive / 132 gold
- SOCKS5: 205 alive / 134 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20045
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
