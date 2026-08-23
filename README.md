# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 377
- HTTP: 109 alive / 43 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 217 alive / 162 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32980
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
