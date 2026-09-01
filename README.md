# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 411
- HTTP: 80 alive / 64 gold
- HTTPS: 86 alive / 22 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47196
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
