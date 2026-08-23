# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 368
- HTTP: 81 alive / 44 gold
- HTTPS: 33 alive / 10 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 190 alive / 157 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33010
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
