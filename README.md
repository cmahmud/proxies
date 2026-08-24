# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 385
- HTTP: 92 alive / 52 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33488
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
