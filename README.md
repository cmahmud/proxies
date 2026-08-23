# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 366
- HTTP: 68 alive / 41 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33008
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
