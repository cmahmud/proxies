# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 257
- HTTP: 62 alive / 53 gold
- HTTPS: 253 alive / 27 gold
- SOCKS4: 55 alive / 43 gold
- SOCKS5: 139 alive / 134 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48457
- Ever gold: 1538

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
