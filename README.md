# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 407
- HTTP: 110 alive / 64 gold
- HTTPS: 53 alive / 16 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33679
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
