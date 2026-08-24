# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 430
- HTTP: 119 alive / 80 gold
- HTTPS: 99 alive / 22 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34023
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
