# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 441
- HTTP: 120 alive / 84 gold
- HTTPS: 100 alive / 23 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34316
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
