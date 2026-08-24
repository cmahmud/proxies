# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 434
- HTTP: 135 alive / 80 gold
- HTTPS: 62 alive / 23 gold
- SOCKS4: 190 alive / 161 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33953
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
