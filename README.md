# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 438
- HTTP: 135 alive / 82 gold
- HTTPS: 97 alive / 24 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34372
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
