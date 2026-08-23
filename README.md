# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 353
- HTTP: 89 alive / 33 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 171826
- Ever alive: 32949
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
