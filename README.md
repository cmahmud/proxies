# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 371
- HTTP: 86 alive / 44 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 180 alive / 157 gold
- SOCKS5: 198 alive / 160 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32978
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
