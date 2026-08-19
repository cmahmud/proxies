# SyndProxy private pool

## Current pool

- Alive now: 1279
- Gold now: 400
- HTTP: 425 alive / 90 gold
- HTTPS: 283 alive / 16 gold
- SOCKS4: 236 alive / 129 gold
- SOCKS5: 335 alive / 165 gold

## Historical pool

- Discovered: 133936
- Ever alive: 21454
- Ever gold: 881

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
