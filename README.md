# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 371
- HTTP: 82 alive / 45 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 194 alive / 160 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32977
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
