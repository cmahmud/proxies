# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 421
- HTTP: 111 alive / 74 gold
- HTTPS: 52 alive / 20 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44509
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
