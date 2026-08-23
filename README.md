# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 382
- HTTP: 115 alive / 58 gold
- HTTPS: 33 alive / 10 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 183 alive / 159 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33103
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
