# SyndProxy validated proxy pool

## Current pool

- Alive now: 442
- Gold now: 360
- HTTP: 86 alive / 64 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 154 alive / 133 gold
- SOCKS5: 162 alive / 147 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49558
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
