# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 393
- HTTP: 131 alive / 60 gold
- HTTPS: 50 alive / 11 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 201 alive / 164 gold

## Historical pool

- Discovered: 178292
- Ever alive: 33373
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
