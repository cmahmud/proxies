# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 485
- HTTP: 152 alive / 102 gold
- HTTPS: 125 alive / 43 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 198 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44952
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
