# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 416
- HTTP: 105 alive / 65 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 200 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36041
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
