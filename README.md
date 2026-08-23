# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 376
- HTTP: 98 alive / 48 gold
- HTTPS: 38 alive / 13 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32959
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
