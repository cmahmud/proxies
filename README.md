# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 374
- HTTP: 93 alive / 44 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 181 alive / 158 gold
- SOCKS5: 200 alive / 161 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32977
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
