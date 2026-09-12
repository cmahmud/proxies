# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 461
- HTTP: 130 alive / 93 gold
- HTTPS: 58 alive / 32 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49406
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
