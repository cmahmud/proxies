# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 455
- HTTP: 127 alive / 86 gold
- HTTPS: 115 alive / 34 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45619
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
