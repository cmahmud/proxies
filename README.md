# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 445
- HTTP: 124 alive / 80 gold
- HTTPS: 77 alive / 31 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45560
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
