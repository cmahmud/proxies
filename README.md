# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 424
- HTTP: 112 alive / 68 gold
- HTTPS: 96 alive / 22 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36037
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
