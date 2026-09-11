# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 425
- HTTP: 94 alive / 71 gold
- HTTPS: 57 alive / 25 gold
- SOCKS4: 198 alive / 168 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49087
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
