# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 386
- HTTP: 82 alive / 62 gold
- HTTPS: 35 alive / 14 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 176 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48129
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
