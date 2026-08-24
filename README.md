# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 391
- HTTP: 106 alive / 54 gold
- HTTPS: 51 alive / 14 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 203 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33382
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
