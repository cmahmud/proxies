# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 372
- HTTP: 90 alive / 44 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 199 alive / 160 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32977
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
