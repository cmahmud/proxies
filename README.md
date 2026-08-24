# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 443
- HTTP: 115 alive / 84 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34198
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
