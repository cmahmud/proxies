# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 385
- HTTP: 94 alive / 56 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33465
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
