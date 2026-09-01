# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 408
- HTTP: 85 alive / 64 gold
- HTTPS: 81 alive / 22 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47198
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
