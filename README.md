# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 448
- HTTP: 95 alive / 77 gold
- HTTPS: 110 alive / 31 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47427
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
