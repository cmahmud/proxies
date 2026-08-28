# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 362
- HTTP: 101 alive / 65 gold
- HTTPS: 71 alive / 8 gold
- SOCKS4: 161 alive / 142 gold
- SOCKS5: 173 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43175
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
