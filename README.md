# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 460
- HTTP: 126 alive / 86 gold
- HTTPS: 126 alive / 34 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46800
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
