# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 433
- HTTP: 134 alive / 79 gold
- HTTPS: 92 alive / 21 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34454
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
