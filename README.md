# SyndProxy validated proxy pool

## Current pool

- Alive now: 442
- Gold now: 363
- HTTP: 69 alive / 42 gold
- HTTPS: 32 alive / 10 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 178 alive / 155 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33020
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
