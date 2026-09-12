# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 447
- HTTP: 118 alive / 91 gold
- HTTPS: 50 alive / 30 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49304
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
