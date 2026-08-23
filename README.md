# SyndProxy validated proxy pool

## Current pool

- Alive now: 444
- Gold now: 362
- HTTP: 68 alive / 43 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 163 alive / 154 gold
- SOCKS5: 177 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33017
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
