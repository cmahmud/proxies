# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 410
- HTTP: 87 alive / 64 gold
- HTTPS: 92 alive / 22 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47200
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
