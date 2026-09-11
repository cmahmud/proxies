# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 426
- HTTP: 99 alive / 72 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 198 alive / 167 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49081
- Ever gold: 1572

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
