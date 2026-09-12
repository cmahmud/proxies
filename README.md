# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 441
- HTTP: 117 alive / 84 gold
- HTTPS: 57 alive / 27 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49270
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
