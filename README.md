# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 455
- HTTP: 124 alive / 81 gold
- HTTPS: 101 alive / 38 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46980
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
