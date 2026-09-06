# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 342
- HTTP: 77 alive / 51 gold
- HTTPS: 32 alive / 7 gold
- SOCKS4: 165 alive / 140 gold
- SOCKS5: 178 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48289
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
