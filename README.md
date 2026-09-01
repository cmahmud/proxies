# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 472
- HTTP: 144 alive / 93 gold
- HTTPS: 118 alive / 42 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46968
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
