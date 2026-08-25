# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 425
- HTTP: 101 alive / 64 gold
- HTTPS: 77 alive / 22 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 216 alive / 178 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35894
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
