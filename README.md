# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 439
- HTTP: 123 alive / 80 gold
- HTTPS: 97 alive / 24 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 204 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45457
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
