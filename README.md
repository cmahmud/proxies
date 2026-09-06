# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 387
- HTTP: 88 alive / 63 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48129
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
