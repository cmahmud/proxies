# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 416
- HTTP: 241 alive / 98 gold
- HTTPS: 200 alive / 25 gold
- SOCKS4: 214 alive / 136 gold
- SOCKS5: 244 alive / 157 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27598
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
