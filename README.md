# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 318
- HTTP: 45 alive / 28 gold
- HTTPS: 14 alive / 1 gold
- SOCKS4: 160 alive / 146 gold
- SOCKS5: 165 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43599
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
