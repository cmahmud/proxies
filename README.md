# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 441
- HTTP: 107 alive / 87 gold
- HTTPS: 57 alive / 30 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49429
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
