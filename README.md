# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 439
- HTTP: 129 alive / 83 gold
- HTTPS: 95 alive / 24 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33994
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
