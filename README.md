# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 380
- HTTP: 96 alive / 46 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 210 alive / 162 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32981
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
