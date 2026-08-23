# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 376
- HTTP: 109 alive / 58 gold
- HTTPS: 29 alive / 11 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 174348
- Ever alive: 33086
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
