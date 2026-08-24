# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 430
- HTTP: 124 alive / 80 gold
- HTTPS: 111 alive / 22 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34040
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
