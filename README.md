# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 377
- HTTP: 93 alive / 62 gold
- HTTPS: 35 alive / 12 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 174159
- Ever alive: 33077
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
