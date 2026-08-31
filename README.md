# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 449
- HTTP: 122 alive / 84 gold
- HTTPS: 82 alive / 33 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 201 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45576
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
