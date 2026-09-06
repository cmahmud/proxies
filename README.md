# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 385
- HTTP: 90 alive / 63 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 170 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48166
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
