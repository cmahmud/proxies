# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 429
- HTTP: 134 alive / 80 gold
- HTTPS: 69 alive / 21 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33945
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
