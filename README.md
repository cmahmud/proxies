# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 381
- HTTP: 97 alive / 64 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 174159
- Ever alive: 33077
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
