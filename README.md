# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 429
- HTTP: 108 alive / 78 gold
- HTTPS: 123 alive / 20 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42446
- Ever gold: 1356

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
