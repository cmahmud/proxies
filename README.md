# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 383
- HTTP: 103 alive / 57 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 178 alive / 159 gold

## Historical pool

- Discovered: 175389
- Ever alive: 33124
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
