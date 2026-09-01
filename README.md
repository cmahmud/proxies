# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 467
- HTTP: 140 alive / 94 gold
- HTTPS: 124 alive / 35 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46891
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
