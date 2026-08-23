# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 366
- HTTP: 82 alive / 43 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32990
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
