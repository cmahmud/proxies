# SyndProxy validated proxy pool

## Current pool

- Alive now: 677
- Gold now: 465
- HTTP: 167 alive / 96 gold
- HTTPS: 111 alive / 35 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 227 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45306
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
