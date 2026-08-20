# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 562
- HTTP: 430 alive / 182 gold
- HTTPS: 306 alive / 91 gold
- SOCKS4: 222 alive / 132 gold
- SOCKS5: 243 alive / 157 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22955
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
