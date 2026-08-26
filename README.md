# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 402
- HTTP: 90 alive / 60 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38979
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
