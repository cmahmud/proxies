# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 435
- HTTP: 129 alive / 80 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34692
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
