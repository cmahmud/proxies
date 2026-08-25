# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 416
- HTTP: 84 alive / 61 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36192
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
