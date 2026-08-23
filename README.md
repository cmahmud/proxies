# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 351
- HTTP: 126 alive / 33 gold
- HTTPS: 31 alive / 8 gold
- SOCKS4: 174 alive / 153 gold
- SOCKS5: 186 alive / 157 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32953
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
