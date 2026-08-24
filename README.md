# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 435
- HTTP: 128 alive / 78 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 185 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34687
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
