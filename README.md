# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 404
- HTTP: 96 alive / 59 gold
- HTTPS: 77 alive / 16 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39110
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
