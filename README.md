# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 386
- HTTP: 88 alive / 52 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33493
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
