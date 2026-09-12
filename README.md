# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 466
- HTTP: 134 alive / 100 gold
- HTTPS: 64 alive / 34 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49338
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
