# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 349
- HTTP: 110 alive / 78 gold
- HTTPS: 51 alive / 25 gold
- SOCKS4: 80 alive / 74 gold
- SOCKS5: 181 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48665
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
