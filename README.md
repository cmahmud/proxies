# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 437
- HTTP: 137 alive / 81 gold
- HTTPS: 98 alive / 24 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34370
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
