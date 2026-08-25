# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 424
- HTTP: 107 alive / 67 gold
- HTTPS: 102 alive / 25 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35661
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
