# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 464
- HTTP: 165 alive / 93 gold
- HTTPS: 120 alive / 35 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 222 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45311
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
