# SyndProxy private pool

## Current pool

- Alive now: 758
- Gold now: 267
- HTTP: 201 alive / 33 gold
- HTTPS: 151 alive / 4 gold
- SOCKS4: 213 alive / 132 gold
- SOCKS5: 193 alive / 98 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10663
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
