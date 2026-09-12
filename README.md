# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 361
- HTTP: 88 alive / 64 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 157 alive / 135 gold
- SOCKS5: 160 alive / 146 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49558
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
