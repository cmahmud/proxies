# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 375
- HTTP: 110 alive / 46 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33539
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
