# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 375
- HTTP: 85 alive / 59 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 180 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48129
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
