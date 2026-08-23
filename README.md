# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 348
- HTTP: 127 alive / 33 gold
- HTTPS: 38 alive / 8 gold
- SOCKS4: 179 alive / 152 gold
- SOCKS5: 194 alive / 155 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32951
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
