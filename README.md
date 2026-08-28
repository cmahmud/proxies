# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 392
- HTTP: 76 alive / 58 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 171 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42905
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
