# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 442
- HTTP: 125 alive / 79 gold
- HTTPS: 142 alive / 33 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44712
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
