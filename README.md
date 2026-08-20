# SyndProxy private pool

## Current pool

- Alive now: 721
- Gold now: 359
- HTTP: 189 alive / 68 gold
- HTTPS: 138 alive / 15 gold
- SOCKS4: 186 alive / 134 gold
- SOCKS5: 208 alive / 142 gold

## Historical pool

- Discovered: 149498
- Ever alive: 26696
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
