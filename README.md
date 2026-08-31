# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 441
- HTTP: 111 alive / 79 gold
- HTTPS: 109 alive / 29 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45637
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
