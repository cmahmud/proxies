# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 449
- HTTP: 119 alive / 83 gold
- HTTPS: 104 alive / 32 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45645
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
