# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 436
- HTTP: 123 alive / 81 gold
- HTTPS: 64 alive / 28 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43696
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
