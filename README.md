# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 368
- HTTP: 70 alive / 42 gold
- HTTPS: 37 alive / 10 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 183 alive / 159 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33008
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
