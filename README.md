# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 379
- HTTP: 128 alive / 68 gold
- HTTPS: 69 alive / 13 gold
- SOCKS4: 163 alive / 149 gold
- SOCKS5: 180 alive / 149 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33231
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
