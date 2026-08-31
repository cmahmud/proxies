# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 439
- HTTP: 149 alive / 77 gold
- HTTPS: 103 alive / 29 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 216 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45412
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
