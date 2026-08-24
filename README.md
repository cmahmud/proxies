# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 435
- HTTP: 140 alive / 81 gold
- HTTPS: 97 alive / 21 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34445
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
