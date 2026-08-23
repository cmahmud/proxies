# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 389
- HTTP: 135 alive / 62 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 185 alive / 154 gold
- SOCKS5: 193 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33192
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
