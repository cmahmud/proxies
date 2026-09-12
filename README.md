# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 444
- HTTP: 114 alive / 86 gold
- HTTPS: 54 alive / 28 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49272
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
