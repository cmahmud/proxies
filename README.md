# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 382
- HTTP: 118 alive / 66 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 152 alive / 142 gold
- SOCKS5: 172 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38924
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
