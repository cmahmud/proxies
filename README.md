# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 396
- HTTP: 96 alive / 60 gold
- HTTPS: 172 alive / 13 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40647
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
