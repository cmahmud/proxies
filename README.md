# SyndProxy validated proxy pool

## Current pool

- Alive now: 442
- Gold now: 354
- HTTP: 120 alive / 78 gold
- HTTPS: 51 alive / 27 gold
- SOCKS4: 82 alive / 75 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48656
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
