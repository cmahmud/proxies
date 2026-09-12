# SyndProxy validated proxy pool

## Current pool

- Alive now: 455
- Gold now: 363
- HTTP: 93 alive / 65 gold
- HTTPS: 43 alive / 16 gold
- SOCKS4: 158 alive / 135 gold
- SOCKS5: 161 alive / 147 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49558
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
