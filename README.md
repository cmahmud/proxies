# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 460
- HTTP: 121 alive / 85 gold
- HTTPS: 100 alive / 41 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46973
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
