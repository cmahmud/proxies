# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 426
- HTTP: 109 alive / 68 gold
- HTTPS: 93 alive / 22 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 200 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36037
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
