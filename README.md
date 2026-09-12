# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 441
- HTTP: 118 alive / 85 gold
- HTTPS: 46 alive / 27 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49273
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
