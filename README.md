# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 444
- HTTP: 147 alive / 81 gold
- HTTPS: 103 alive / 29 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 211 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45449
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
