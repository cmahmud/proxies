# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 414
- HTTP: 90 alive / 62 gold
- HTTPS: 70 alive / 19 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36255
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
