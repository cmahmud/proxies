# SyndProxy private pool

## Current pool

- Alive now: 1320
- Gold now: 562
- HTTP: 536 alive / 189 gold
- HTTPS: 343 alive / 96 gold
- SOCKS4: 231 alive / 144 gold
- SOCKS5: 210 alive / 133 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22790
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
