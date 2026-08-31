# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 444
- HTTP: 137 alive / 80 gold
- HTTPS: 94 alive / 29 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 208 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45451
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
