# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 378
- HTTP: 111 alive / 54 gold
- HTTPS: 31 alive / 10 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
