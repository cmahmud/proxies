# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 385
- HTTP: 105 alive / 61 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
