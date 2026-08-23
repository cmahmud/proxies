# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 380
- HTTP: 99 alive / 45 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 213 alive / 162 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32980
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
