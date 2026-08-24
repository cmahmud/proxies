# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 430
- HTTP: 137 alive / 81 gold
- HTTPS: 96 alive / 22 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34074
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
