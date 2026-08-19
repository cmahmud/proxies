# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 348
- HTTP: 288 alive / 62 gold
- HTTPS: 242 alive / 19 gold
- SOCKS4: 233 alive / 145 gold
- SOCKS5: 212 alive / 122 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15384
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
