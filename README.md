# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 383
- HTTP: 123 alive / 45 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33580
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
