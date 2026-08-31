# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 419
- HTTP: 97 alive / 64 gold
- HTTPS: 63 alive / 25 gold
- SOCKS4: 171 alive / 164 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45488
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
