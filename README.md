# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 378
- HTTP: 79 alive / 54 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 178 alive / 159 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33104
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
