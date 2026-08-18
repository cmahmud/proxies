# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 350
- HTTP: 300 alive / 51 gold
- HTTPS: 190 alive / 14 gold
- SOCKS4: 248 alive / 145 gold
- SOCKS5: 234 alive / 140 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14717
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
