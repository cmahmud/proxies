# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 412
- HTTP: 90 alive / 57 gold
- HTTPS: 69 alive / 19 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36276
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
