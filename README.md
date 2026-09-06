# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 373
- HTTP: 82 alive / 58 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 178 alive / 151 gold
- SOCKS5: 180 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48129
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
