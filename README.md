# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 435
- HTTP: 112 alive / 78 gold
- HTTPS: 81 alive / 24 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34101
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
