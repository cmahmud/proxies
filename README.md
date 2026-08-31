# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 419
- HTTP: 94 alive / 63 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45489
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
