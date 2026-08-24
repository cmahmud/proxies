# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 385
- HTTP: 108 alive / 55 gold
- HTTPS: 58 alive / 11 gold
- SOCKS4: 184 alive / 158 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33479
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
