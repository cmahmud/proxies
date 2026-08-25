# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 416
- HTTP: 94 alive / 62 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36119
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
