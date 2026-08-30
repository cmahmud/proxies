# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 425
- HTTP: 117 alive / 79 gold
- HTTPS: 47 alive / 21 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44479
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
