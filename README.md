# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 379
- HTTP: 88 alive / 44 gold
- HTTPS: 56 alive / 12 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33566
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
