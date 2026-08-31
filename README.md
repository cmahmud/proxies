# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 445
- HTTP: 147 alive / 83 gold
- HTTPS: 118 alive / 30 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 214 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45425
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
