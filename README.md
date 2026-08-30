# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 490
- HTTP: 152 alive / 104 gold
- HTTPS: 127 alive / 46 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 194 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44955
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
