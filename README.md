# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 418
- HTTP: 87 alive / 62 gold
- HTTPS: 71 alive / 22 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36102
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
