# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 389
- HTTP: 107 alive / 62 gold
- HTTPS: 57 alive / 14 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33169
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
