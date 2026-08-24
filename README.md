# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 385
- HTTP: 107 alive / 54 gold
- HTTPS: 61 alive / 11 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33478
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
