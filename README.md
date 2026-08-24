# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 379
- HTTP: 96 alive / 54 gold
- HTTPS: 34 alive / 12 gold
- SOCKS4: 172 alive / 152 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33467
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
