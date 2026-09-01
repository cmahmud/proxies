# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 460
- HTTP: 122 alive / 85 gold
- HTTPS: 103 alive / 41 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46973
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
