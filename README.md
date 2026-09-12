# SyndProxy validated proxy pool

## Current pool

- Alive now: 437
- Gold now: 357
- HTTP: 85 alive / 63 gold
- HTTPS: 39 alive / 16 gold
- SOCKS4: 153 alive / 133 gold
- SOCKS5: 160 alive / 145 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49558
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
