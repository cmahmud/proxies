# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 402
- HTTP: 180 alive / 72 gold
- HTTPS: 60 alive / 15 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33285
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
