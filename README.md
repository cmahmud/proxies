# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 443
- HTTP: 117 alive / 84 gold
- HTTPS: 75 alive / 25 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34178
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
