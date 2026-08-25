# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 419
- HTTP: 83 alive / 62 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36185
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
