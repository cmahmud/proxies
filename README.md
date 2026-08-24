# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 436
- HTTP: 127 alive / 79 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 186 alive / 173 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34136
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
