# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 442
- HTTP: 118 alive / 86 gold
- HTTPS: 46 alive / 28 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49243
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
