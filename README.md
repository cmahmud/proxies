# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 427
- HTTP: 97 alive / 74 gold
- HTTPS: 64 alive / 26 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44430
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
