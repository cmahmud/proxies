# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 461
- HTTP: 136 alive / 89 gold
- HTTPS: 120 alive / 36 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46902
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
