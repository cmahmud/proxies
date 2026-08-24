# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 434
- HTTP: 113 alive / 78 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34104
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
