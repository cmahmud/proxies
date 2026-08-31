# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 451
- HTTP: 128 alive / 81 gold
- HTTPS: 120 alive / 34 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45629
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
