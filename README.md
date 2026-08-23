# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 362
- HTTP: 112 alive / 38 gold
- HTTPS: 57 alive / 8 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 193 alive / 155 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32924
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
