# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 389
- HTTP: 130 alive / 64 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 176 alive / 158 gold

## Historical pool

- Discovered: 175416
- Ever alive: 33128
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
