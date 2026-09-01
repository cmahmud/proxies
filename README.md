# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 455
- HTTP: 126 alive / 84 gold
- HTTPS: 104 alive / 38 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46979
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
