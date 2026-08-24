# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 381
- HTTP: 100 alive / 43 gold
- HTTPS: 49 alive / 12 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33562
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
