# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 421
- HTTP: 99 alive / 61 gold
- HTTPS: 70 alive / 32 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45494
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
