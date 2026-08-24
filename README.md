# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 387
- HTTP: 130 alive / 55 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 178 alive / 157 gold
- SOCKS5: 201 alive / 163 gold

## Historical pool

- Discovered: 178292
- Ever alive: 33368
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
