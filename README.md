# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 429
- HTTP: 91 alive / 74 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 184 alive / 168 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49091
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
