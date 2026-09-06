# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 316
- HTTP: 77 alive / 52 gold
- HTTPS: 32 alive / 11 gold
- SOCKS4: 148 alive / 133 gold
- SOCKS5: 142 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48332
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
