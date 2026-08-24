# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 443
- HTTP: 122 alive / 83 gold
- HTTPS: 74 alive / 26 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34721
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
