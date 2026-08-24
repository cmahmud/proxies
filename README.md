# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 435
- HTTP: 113 alive / 78 gold
- HTTPS: 71 alive / 24 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34097
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
