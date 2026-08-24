# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 436
- HTTP: 132 alive / 79 gold
- HTTPS: 104 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34340
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
