# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 411
- HTTP: 79 alive / 64 gold
- HTTPS: 92 alive / 21 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47180
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
