# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 433
- HTTP: 124 alive / 81 gold
- HTTPS: 71 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33928
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
