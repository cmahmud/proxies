# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 421
- HTTP: 115 alive / 75 gold
- HTTPS: 47 alive / 21 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 192 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44476
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
