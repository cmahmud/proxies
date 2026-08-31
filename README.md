# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 451
- HTTP: 135 alive / 84 gold
- HTTPS: 95 alive / 36 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45584
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
