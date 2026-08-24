# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 388
- HTTP: 113 alive / 69 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33243
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
