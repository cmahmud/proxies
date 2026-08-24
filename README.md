# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 373
- HTTP: 123 alive / 51 gold
- HTTPS: 44 alive / 7 gold
- SOCKS4: 176 alive / 155 gold
- SOCKS5: 193 alive / 160 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33449
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
