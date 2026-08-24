# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 394
- HTTP: 132 alive / 60 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 202 alive / 165 gold

## Historical pool

- Discovered: 178292
- Ever alive: 33369
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
