# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 438
- HTTP: 122 alive / 75 gold
- HTTPS: 91 alive / 28 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 203 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45456
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
