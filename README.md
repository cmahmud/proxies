# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 356
- HTTP: 89 alive / 67 gold
- HTTPS: 33 alive / 17 gold
- SOCKS4: 147 alive / 126 gold
- SOCKS5: 160 alive / 146 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49554
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
