# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 416
- HTTP: 88 alive / 62 gold
- HTTPS: 76 alive / 21 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36094
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
