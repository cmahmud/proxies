# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 393
- HTTP: 68 alive / 57 gold
- HTTPS: 72 alive / 14 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42889
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
