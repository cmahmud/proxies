# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 410
- HTTP: 75 alive / 54 gold
- HTTPS: 42 alive / 22 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47102
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
