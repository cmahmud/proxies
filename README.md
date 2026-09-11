# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 419
- HTTP: 100 alive / 73 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49003
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
