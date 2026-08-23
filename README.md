# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 375
- HTTP: 91 alive / 62 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 173 alive / 153 gold

## Historical pool

- Discovered: 174307
- Ever alive: 33078
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
