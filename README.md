# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 443
- HTTP: 132 alive / 86 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34413
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
