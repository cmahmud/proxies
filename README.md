# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 370
- HTTP: 85 alive / 44 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 191 alive / 160 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32977
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
