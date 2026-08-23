# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 376
- HTTP: 100 alive / 59 gold
- HTTPS: 29 alive / 10 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 172 alive / 156 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33086
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
