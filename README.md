# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 423
- HTTP: 77 alive / 66 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47146
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
