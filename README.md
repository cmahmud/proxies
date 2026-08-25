# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 416
- HTTP: 90 alive / 64 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36255
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
