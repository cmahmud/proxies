# SyndProxy validated proxy pool

## Current pool

- Alive now: 443
- Gold now: 358
- HTTP: 87 alive / 64 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 156 alive / 133 gold
- SOCKS5: 160 alive / 146 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49558
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
