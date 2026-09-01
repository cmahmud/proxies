# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 471
- HTTP: 130 alive / 91 gold
- HTTPS: 117 alive / 44 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46962
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
