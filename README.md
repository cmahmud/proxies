# SyndProxy validated proxy pool

## Current pool

- Alive now: 368
- Gold now: 193
- HTTP: 119 alive / 38 gold
- HTTPS: 59 alive / 8 gold
- SOCKS4: 70 alive / 62 gold
- SOCKS5: 120 alive / 85 gold

## Historical pool

- Discovered: 170124
- Ever alive: 32716
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
