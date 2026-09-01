# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 467
- HTTP: 127 alive / 91 gold
- HTTPS: 106 alive / 41 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46965
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
