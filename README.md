# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 429
- HTTP: 115 alive / 70 gold
- HTTPS: 67 alive / 22 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36024
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
