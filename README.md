# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 418
- HTTP: 92 alive / 70 gold
- HTTPS: 109 alive / 19 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42530
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
