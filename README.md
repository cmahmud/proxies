# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 438
- HTTP: 146 alive / 83 gold
- HTTPS: 95 alive / 22 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33980
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
