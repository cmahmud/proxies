# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 377
- HTTP: 87 alive / 45 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33556
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
