# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 423
- HTTP: 88 alive / 64 gold
- HTTPS: 78 alive / 27 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47158
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
