# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 439
- HTTP: 129 alive / 86 gold
- HTTPS: 95 alive / 21 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34420
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
