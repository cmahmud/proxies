# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 434
- HTTP: 107 alive / 75 gold
- HTTPS: 68 alive / 30 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47024
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
