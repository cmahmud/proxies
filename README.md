# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 471
- HTTP: 147 alive / 93 gold
- HTTPS: 115 alive / 41 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46968
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
