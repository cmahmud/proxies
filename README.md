# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 446
- HTTP: 117 alive / 91 gold
- HTTPS: 49 alive / 27 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49300
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
