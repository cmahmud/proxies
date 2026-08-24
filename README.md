# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 435
- HTTP: 123 alive / 80 gold
- HTTPS: 80 alive / 24 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34004
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
