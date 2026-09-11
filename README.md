# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 423
- HTTP: 102 alive / 71 gold
- HTTPS: 62 alive / 24 gold
- SOCKS4: 183 alive / 166 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49022
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
