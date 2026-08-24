# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 392
- HTTP: 112 alive / 58 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33500
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
