# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 400
- HTTP: 121 alive / 67 gold
- HTTPS: 59 alive / 10 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33311
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
