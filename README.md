# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 392
- HTTP: 98 alive / 56 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33356
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
