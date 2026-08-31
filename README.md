# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 427
- HTTP: 94 alive / 70 gold
- HTTPS: 66 alive / 28 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45479
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
