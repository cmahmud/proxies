# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 385
- HTTP: 117 alive / 70 gold
- HTTPS: 102 alive / 13 gold
- SOCKS4: 167 alive / 149 gold
- SOCKS5: 187 alive / 153 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33235
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
