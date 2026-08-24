# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 441
- HTTP: 164 alive / 83 gold
- HTTPS: 72 alive / 25 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34732
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
