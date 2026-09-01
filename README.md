# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 458
- HTTP: 123 alive / 88 gold
- HTTPS: 115 alive / 34 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46715
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
