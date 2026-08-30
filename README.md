# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 450
- HTTP: 116 alive / 89 gold
- HTTPS: 53 alive / 32 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 176 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43676
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
