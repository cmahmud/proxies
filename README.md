# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 407
- HTTP: 90 alive / 67 gold
- HTTPS: 33 alive / 21 gold
- SOCKS4: 159 alive / 146 gold
- SOCKS5: 185 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48796
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
