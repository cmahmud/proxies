# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 433
- HTTP: 126 alive / 77 gold
- HTTPS: 101 alive / 23 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34481
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
