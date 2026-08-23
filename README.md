# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 344
- HTTP: 125 alive / 31 gold
- HTTPS: 34 alive / 8 gold
- SOCKS4: 178 alive / 151 gold
- SOCKS5: 200 alive / 154 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32950
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
