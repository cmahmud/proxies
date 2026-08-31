# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 479
- HTTP: 154 alive / 99 gold
- HTTPS: 140 alive / 41 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 200 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45219
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
