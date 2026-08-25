# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 417
- HTTP: 82 alive / 60 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36181
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
