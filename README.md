# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 434
- HTTP: 105 alive / 74 gold
- HTTPS: 63 alive / 30 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47024
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
