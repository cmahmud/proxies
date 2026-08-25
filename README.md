# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 412
- HTTP: 100 alive / 59 gold
- HTTPS: 67 alive / 19 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 198 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36220
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
