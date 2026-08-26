# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 410
- HTTP: 99 alive / 65 gold
- HTTPS: 77 alive / 16 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39238
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
