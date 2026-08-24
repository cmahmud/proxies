# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 428
- HTTP: 125 alive / 80 gold
- HTTPS: 101 alive / 22 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34062
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
