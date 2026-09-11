# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 408
- HTTP: 90 alive / 62 gold
- HTTPS: 38 alive / 21 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 179 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48821
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
