# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 433
- HTTP: 129 alive / 79 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34477
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
