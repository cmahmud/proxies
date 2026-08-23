# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 357
- HTTP: 86 alive / 35 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 171794
- Ever alive: 32947
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
