# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 436
- HTTP: 130 alive / 79 gold
- HTTPS: 90 alive / 24 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34675
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
