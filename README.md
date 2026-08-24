# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 378
- HTTP: 130 alive / 68 gold
- HTTPS: 55 alive / 14 gold
- SOCKS4: 172 alive / 148 gold
- SOCKS5: 178 alive / 148 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33221
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
