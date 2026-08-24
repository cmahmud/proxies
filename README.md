# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 393
- HTTP: 93 alive / 55 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33490
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
