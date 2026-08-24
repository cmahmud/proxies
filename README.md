# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 443
- HTTP: 120 alive / 84 gold
- HTTPS: 78 alive / 25 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34177
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
