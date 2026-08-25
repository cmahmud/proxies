# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 410
- HTTP: 94 alive / 62 gold
- HTTPS: 77 alive / 22 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37031
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
