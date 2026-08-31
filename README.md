# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 427
- HTTP: 95 alive / 71 gold
- HTTPS: 61 alive / 27 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45479
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
