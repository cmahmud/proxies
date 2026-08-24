# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 382
- HTTP: 95 alive / 55 gold
- HTTPS: 35 alive / 12 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33465
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
