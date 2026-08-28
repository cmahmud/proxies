# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 402
- HTTP: 70 alive / 53 gold
- HTTPS: 68 alive / 23 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42774
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
