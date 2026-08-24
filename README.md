# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 396
- HTTP: 133 alive / 71 gold
- HTTPS: 62 alive / 15 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 188 alive / 155 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33268
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
