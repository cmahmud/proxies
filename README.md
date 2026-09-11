# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 430
- HTTP: 102 alive / 74 gold
- HTTPS: 53 alive / 26 gold
- SOCKS4: 189 alive / 162 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49131
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
