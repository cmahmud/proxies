# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 430
- HTTP: 100 alive / 74 gold
- HTTPS: 55 alive / 26 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49130
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
