# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 306
- HTTP: 126 alive / 37 gold
- HTTPS: 62 alive / 10 gold
- SOCKS4: 194 alive / 152 gold
- SOCKS5: 183 alive / 107 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32825
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
