# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 451
- HTTP: 121 alive / 82 gold
- HTTPS: 109 alive / 34 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45630
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
