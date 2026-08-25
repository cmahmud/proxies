# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 418
- HTTP: 103 alive / 62 gold
- HTTPS: 77 alive / 20 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35995
- Ever gold: 1262

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
