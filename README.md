# SyndProxy private pool

## Current pool

- Alive now: 1550
- Gold now: 606
- HTTP: 575 alive / 208 gold
- HTTPS: 395 alive / 113 gold
- SOCKS4: 230 alive / 149 gold
- SOCKS5: 350 alive / 136 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23652
- Ever gold: 954

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
