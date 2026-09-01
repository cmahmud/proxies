# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 410
- HTTP: 87 alive / 60 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47081
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
